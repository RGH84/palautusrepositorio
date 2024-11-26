from int_joukko import IntJoukko


def main():
    # Luodaan kaksi joukkoa
    joukko1 = IntJoukko()
    joukko2 = IntJoukko()

    # Lisätään alkioita ensimmäiseen joukkoon
    joukko1.lisaa(1)
    joukko1.lisaa(2)
    joukko1.lisaa(3)
    print("Joukko 1:", joukko1.to_int_list())

    # Lisätään alkioita toiseen joukkoon
    joukko2.lisaa(3)
    joukko2.lisaa(4)
    joukko2.lisaa(5)
    print("Joukko 2:", joukko2.to_int_list())

    # Testataan joukko-operaatiot
    # Yhdiste
    yhdiste = IntJoukko.yhdiste(joukko1, joukko2)
    print("Yhdiste (joukko1 ∪ joukko2):", yhdiste.to_int_list())

    # Leikkaus
    leikkaus = IntJoukko.leikkaus(joukko1, joukko2)
    print("Leikkaus (joukko1 ∩ joukko2):", leikkaus.to_int_list())

    # Erotus
    erotus = IntJoukko.erotus(joukko1, joukko2)
    print("Erotus (joukko1 - joukko2):", erotus.to_int_list())

    # Testataan yksittäisen alkion poistaminen
    joukko1.poista(2)
    print("Joukko 1 poistamisen jälkeen:", joukko1.to_int_list())

    # Testataan alkion lisäämistä
    joukko1.lisaa(6)
    print("Joukko 1 lisäämisen jälkeen:", joukko1.to_int_list())

    # Tulostetaan joukko merkkijonoesityksenä
    print("Joukko 1 (string):", joukko1)
    print("Joukko 2 (string):", joukko2)


if __name__ == "__main__":
    main()
