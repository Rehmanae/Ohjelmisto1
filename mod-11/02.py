"""
Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen,
huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.
"""

class Auto:
    def __init__(self, rekisteri, huippu):
        self.rekisteri = rekisteri
        self.huippu = huippu
        self.nopeus = 0
        self.matka = 0

    def aja(self, tunnit):
        self.matka = self.matka + self.nopeus * tunnit


class Sahkoauto(Auto):
    def __init__(self, rekisteri, huippu, akku):
        Auto.__init__(self, rekisteri, huippu)
        self.akku = akku


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, huippu, tankki):
        Auto.__init__(self, rekisteri, huippu)
        self.tankki = tankki


#pääohjelma
sahko = Sahkoauto("ABC-15", 180, 52.5)
bensa = Polttomoottoriauto("ACD-123", 165, 32.3)

sahko.nopeus = 100
bensa.nopeus = 120

sahko.aja(3)
bensa.aja(3)

print("sahko ajoi", sahko.matka, "km")
print("bensa ajoi", bensa.matka, "km")