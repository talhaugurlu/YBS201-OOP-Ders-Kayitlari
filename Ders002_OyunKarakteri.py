"""YBS201 - OOP: Basit oyun karakteri sinifi ve nesneler."""


class Karakter:
    def __init__(self, isim, can=100, seviye=1):
        self.isim = isim
        self.can = can
        self.seviye = seviye

    def bilgi_goster(self):
        print(f"{self.isim} | Can: {self.can} | Seviye: {self.seviye}")

    def saldir(self):
        print(f"{self.isim} saldırıyor!")


karakter1 = Karakter("Savaşçı")
karakter2 = Karakter("Okçu", 80, 2)

karakter1.bilgi_goster()
karakter1.saldir()
karakter2.bilgi_goster()
karakter2.saldir()
