"""
Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat.
Tee aliluokkiin metodi tulosta_tiedot, joka tulostaa kyseisen julkaisun kaikki tiedot.
Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.
"""

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print("Nimi:", self.nimi)


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivut):
        Julkaisu.__init__(self, nimi)
        self.kirjoittaja = kirjoittaja
        self.sivut = sivut

    def tulosta_tiedot(self):
        print("Kirja:", self.nimi)
        print("Kirjoittaja:", self.kirjoittaja)
        print("Sivuja:", self.sivut)
        print("")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja, sivut):
        Julkaisu.__init__(self, nimi)
        self.paatoimittaja = paatoimittaja
        self.sivut = sivut

    def tulosta_tiedot(self):
        print("Lehti:", self.nimi)
        print("Päätoimittaja:", self.paatoimittaja)
        print("Sivuja:", self.sivut)
        print("")


# pääohjelma
aku_ankka = Lehti("Aku Ankka", "Aki Hyypää", 36)
hytti_kirja = Kirja("Hytin n:o 6", "Rosa Liksom", 200)

aku_ankka.tulosta_tiedot()
hytti_kirja.tulosta_tiedot()
