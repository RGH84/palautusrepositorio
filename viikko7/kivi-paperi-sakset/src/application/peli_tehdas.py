from services.kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from services.kps_tekoaly import KPSTekoaly
from services.kps_parempi_tekoaly import KPSParempiTekoaly


def luo_peli(tyyppi):
    if tyyppi == "a":
        return KPSPelaajaVsPelaaja()
    elif tyyppi == "b":
        return KPSTekoaly()
    elif tyyppi == "c":
        return KPSParempiTekoaly()
    else:
        return None
