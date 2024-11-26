KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def _luo_lista(self, koko):
        """Luo kiinteäkokoinen lista."""
        return [0] * koko

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self._validoi_parametri(
            kapasiteetti, KAPASITEETTI, "Kapasiteetin")
        self.kasvatuskoko = self._validoi_parametri(
            kasvatuskoko, OLETUSKASVATUS, "Kasvatuskoon")
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def _validoi_parametri(self, parametri, oletusarvo, nimi):
        """Tarkistaa, että parametri on kelvollinen ja positiivinen kokonaisluku."""
        if parametri is None:
            return oletusarvo
        if not isinstance(parametri, int) or parametri < 0:
            raise ValueError(f"{nimi} täytyy olla positiivinen kokonaisluku.")
        return parametri

    def kuuluu(self, luku):
        """Tarkistaa, kuuluuko luku joukkoon."""
        return luku in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, luku):
        """Lisää luvun joukkoon, jos se ei jo kuulu siihen."""
        if not self.kuuluu(luku):
            if self.alkioiden_lkm >= len(self.ljono):
                self._kasvata_listaa()
            self.ljono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1
            return True
        return False

    def _kasvata_listaa(self):
        """Kasvattaa joukon tallennustilaa."""
        uusi_ljono = self._luo_lista(len(self.ljono) + self.kasvatuskoko)
        self._kopioi_lista(self.ljono, uusi_ljono)
        self.ljono = uusi_ljono

    def poista(self, luku):
        """Poistaa luvun joukosta, jos se kuuluu siihen."""
        indeksi = self._etsi_indeksi(luku)
        if indeksi != -1:
            self._siirra_lukuja(indeksi)
            self.alkioiden_lkm -= 1
            return True
        return False

    def _etsi_indeksi(self, luku):
        """Etsii luvun indeksin listassa."""
        for i in range(self.alkioiden_lkm):
            if self.ljono[i] == luku:
                return i
        return -1

    def _siirra_lukuja(self, indeksi):
        """Siirtää lukuja poistettavan kohdan jälkeen."""
        for i in range(indeksi, self.alkioiden_lkm - 1):
            self.ljono[i] = self.ljono[i + 1]
        self.ljono[self.alkioiden_lkm - 1] = 0

    def _kopioi_lista(self, alkuperainen, kohde):
        """Kopioi listan toiseen."""
        for i, arvo in enumerate(alkuperainen):
            kohde[i] = arvo

    def mahtavuus(self):
        """Palauttaa joukossa olevien alkioiden lukumäärän."""
        return self.alkioiden_lkm

    def to_int_list(self):
        """Palauttaa joukon alkiot kokonaislukulistana."""
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        """Palauttaa kahden joukon yhdisteen."""
        uusi_joukko = IntJoukko()
        for luku in a.to_int_list() + b.to_int_list():
            uusi_joukko.lisaa(luku)
        return uusi_joukko

    @staticmethod
    def leikkaus(a, b):
        """Palauttaa kahden joukon leikkauksen."""
        uusi_joukko = IntJoukko()
        for luku in a.to_int_list():
            if luku in b.to_int_list():
                uusi_joukko.lisaa(luku)
        return uusi_joukko

    @staticmethod
    def erotus(a, b):
        """Palauttaa kahden joukon erotuksen."""
        uusi_joukko = IntJoukko()
        for luku in a.to_int_list():
            if luku not in b.to_int_list():
                uusi_joukko.lisaa(luku)
        return uusi_joukko

    def __str__(self):
        """Palauttaa joukon merkkijonoesityksen."""
        return "{" + ", ".join(map(str, self.to_int_list())) + "}"
