"""YBS201 - OOP: Futbolcu sinifi, ozellikler ve metotlar."""


class Futbolcu:
    def __init__(self, isim, yas, mevki, guc):
        self.isim = isim
        self.yas = yas
        self.mevki = mevki
        self.guc = guc

    def kos(self):
        print(f"{self.isim} koşuyor.")

    def sut(self, guc):
        print(f"{self.isim} {guc} güçte şut çekti.")


futbolcu1 = Futbolcu("Ahmet", 25, "Forvet", 80)

print(f"Futbolcu {futbolcu1.isim}, {futbolcu1.mevki} mevkisinde oynuyor.")
futbolcu1.kos()
futbolcu1.sut(futbolcu1.guc)
