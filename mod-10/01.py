"""
Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. Hissillä on metodit siirry_kerrokseen,
kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_
kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan
kerrokseen.
"""



class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.nykyinen = alin_kerros

    def ylos(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1
            print("Mennään ylös -> kerros", self.nykyinen)

    def alas(self):
        if self.nykyinen > self.alin:
            self.nykyinen -= 1
            print("Mennään alas -> kerros", self.nykyinen)

    def mene(self, kohde):
        while self.nykyinen != kohde:
            if self.nykyinen < kohde:
                self.ylos()
            else:
                self.alas()


# Pääohjelma
hissi = Hissi(1, 10)
hissi.mene(6)
hissi.mene(1)