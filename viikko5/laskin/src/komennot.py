class Summa:
    def __init__(self, logiikka, lue_syote):
        self._logiikka = logiikka
        self._lue_syote = lue_syote
        self._edellinen_arvo = None

    def suorita(self):
        self._edellinen_arvo = self._logiikka.arvo()
        try:
            arvo = int(self._lue_syote())
        except ValueError:
            arvo = 0
        self._logiikka.plus(arvo)

    def kumoa(self):
        if self._edellinen_arvo is not None:
            self._logiikka.aseta_arvo(self._edellinen_arvo)


class Erotus:
    def __init__(self, logiikka, lue_syote):
        self._logiikka = logiikka
        self._lue_syote = lue_syote
        self._edellinen_arvo = None

    def suorita(self):
        self._edellinen_arvo = self._logiikka.arvo()
        try:
            arvo = int(self._lue_syote())
        except ValueError:
            arvo = 0
        self._logiikka.miinus(arvo)

    def kumoa(self):
        if self._edellinen_arvo is not None:
            self._logiikka.aseta_arvo(self._edellinen_arvo)


class Nollaus:
    def __init__(self, logiikka):
        self._logiikka = logiikka
        self._edellinen_arvo = None

    def suorita(self):
        self._edellinen_arvo = self._logiikka.arvo()
        self._logiikka.nollaa()

    def kumoa(self):
        if self._edellinen_arvo is not None:
            self._logiikka.aseta_arvo(self._edellinen_arvo)


class Kumoa:
    def __init__(self, logiikka):
        self._logiikka = logiikka
        self._viimeisin_komento = None

    def suorita(self, viimeisin_komento):
        self._viimeisin_komento = viimeisin_komento
        if self._viimeisin_komento:
            self._viimeisin_komento.kumoa()
