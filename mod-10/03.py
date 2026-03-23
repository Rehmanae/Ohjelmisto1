"""
Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
 joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

"""

class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def ylos(self):
        if self.kerros < self.ylin:
            self.kerros += 1
            print("Ylös ->", self.kerros)

    def alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
            print("Alas ->", self.kerros)

    def siirry(self, kohde):
        while self.kerros != kohde:
            if self.kerros < kohde:
                self.ylos()
            else:
                self.alas()


class Talo:
    def __init__(self, alin, ylin, lkm):
        self.hissit = []
        for i in range(lkm):
            self.hissit.append(Hissi(alin, ylin))

    def aja(self, nro, kohde):
        print(f"\nHissi {nro} liikkeelle")
        self.hissit[nro].siirry(kohde)

    def palohalytys(self):
        print("\n*** PALOHÄLYTYS ***")
        for i, hissi in enumerate(self.hissit):
            print(f"Hissi {i} palaa alas")
            hissi.siirry(hissi.alin)


# testaus
rakennus = Talo(1, 10, 3)

rakennus.aja(0, 7)
rakennus.aja(2, 4)

rakennus.palohalytys()