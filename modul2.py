import math

def penjumlahan (bil1, bil2):
    hasil = bil1+bil2
    print("hasil penjumlahan dari", bil1, "+", bil2, "adalah", hasil)

def pengurangan (bil1, bil2):
    hasil = bil1-bil2
    print("hasil pengurangan dari", bil1, "-", bil2, "adalah", hasil)

def pembagian (bil1, bil2):
    hasil = bil1/bil2
    print("hasil pembagian dari", bil1, "/", bil2, "adalah", hasil)

def perkalian (bil1, bil2):
    hasil = bil1*bil2
    print("hasil perkalian dari", bil1, "*", bil2, "adalah", hasil)

def pangkat (bil1, bil2):
    hasil = math.pow(bil1, bil2)
    print("hasil pangkat dari", bil1, "^", bil2, "adalah", hasil)

def akar (bil1):
    hasil = math.sqrt(bil1)
    print("hasil dari akar", bil1, "adalah", hasil)

def tan (bil1):
    hasil = math.tan(bil1)
    print("hasil dari tan", bil1, "adalah", hasil)

def cos (bil1):
    hasil = math.cos(bil1)
    print("hasil dari cos", bil1, "adalah", hasil)

def log (bil1):
    hasil = math.log(bil1)
    print("hasil dari log", bil1, "adalah", hasil)

def sin (bil1):
    hasil = math.sin(bil1)
    print("hasil dari sin", bil1, "adalah", hasil)
