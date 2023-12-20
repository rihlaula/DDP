class animals:
    def __init__(self, nama, makanan, hidup, berkembangBiak ):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak

cetak = animals("Ayam", "Beras", "Darat", "Bertelur")
print(f"Nama: {cetak.nama}")
print(f"Makanan : {cetak.makanan}")
print(f"Hidup : {cetak.hidup}")
print(f"Berkembang Biak : {cetak.berkembangBiak}")

print("-------------------------------------------")

class Badak(animals):
    #properti
    def _init_(self, nama, makanan, hidup, berkembangBiak):
        super()._init_(nama, makanan, hidup, berkembangBiak)
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak
    #method
    def hewan(self):
        print(f"Hewan ini adalah {self.nama} \nIa memakan sebuah {self.makanan} \nHidupnya di {self.hidup} \nCara berkembang biak secara {self.berkembangBiak}")

class Ikan(animals):
    #properti
    def _init_(self, nama, makanan, hidup, berkembangBiak):
        super()._init_(nama, makanan, hidup, berkembangBiak)
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak
    #method
    def hewan(self):
        print(f"Hewan ini adalah {self.nama} \nIa memakan sebuah {self.makanan} \nHidupnya di {self.hidup} \nCara berkembang biak secara {self.berkembangBiak}")

class Ular(animals):
    #properti
    def _init_(self, nama, makanan, hidup, berkembangBiak):
        super()._init_(nama, makanan, hidup, berkembangBiak)
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak
    #method
    def hewan(self):
        print(f"Hewan ini adalah {self.nama} \nIa memakan sebuah {self.makanan} \nHidupnya di {self.hidup} \nCara berkembang biak secara {self.berkembangBiak}")


badak = Badak("Badak Bercula Satu", "bambu", "darat", "melahirkan")
ikan = Ikan("Ikan Patin", "ikan-ikanan", "air", "bertelur")
ular = Ular("Ular Sanca", "mamalia kecil", "daratan", "bertelur")

print("\n")
badak.hewan()

print("=================================================\n")

ikan.hewan()
print("=================================================\n")

ular.hewan()