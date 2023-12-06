def persegi(sisi):
    luas = sisi*sisi
    keliling = 4*sisi
    print("jadi luas dari persegi adalah", luas)
    print("jadi keliling dari persegi adalah", keliling)

def persegi_panjang(panjang, lebar):
    luas = panjang*lebar
    keliling = 2*(panjang+lebar)
    print("jadi luas dari persegi panjang adalah", luas)
    print("jadi keliling dari persegi panjang adalah", keliling)

def segitiga(alas, tinggi, sisi1, sisi2, sisi3):
    luas = 0.5*(alas*tinggi)
    keliling = sisi1+sisi2+sisi3
    print("jadi luas dari segitiga adalah", luas)
    print("jadi keliling dari segitiga adalah", keliling)

def jajar_genjang(alas, tinggi, sisi1, sisi2, sisi3, sisi4 ):
    luas = alas*tinggi
    keliling = sisi1+sisi2+sisi3+sisi4
    print("jadi luas dari jajar genjang adalah", luas)
    print("jadi keliling dari jajar genjang adalah", keliling)

def belah_ketupat(d1, d2, sisi):
    luas = 0.5*(d1*d2)
    keliling = 4*sisi
    print("jadi luas dari belah ketupat adalah", luas)
    print("jadi keliling dari belah ketupat adalah", keliling)

def lingkaran(jari2):
    luas = 3.14*jari2*jari2
    keliling = 2*3.14*jari2
    print("jadi luas dari lingkaran adalah", luas)
    print("jadi keliling dari lingkaran adalah", keliling)

def layang_layang(d1, d2, sisi1, sisi2, sisi3, sisi4):
    luas = 0.5*(d1*d2)
    keliling = sisi1+sisi2+sisi3+sisi4
    print("jadi luas dari layang layang adalah", luas)
    print("jadi keliling dari layang layang adalah", keliling)


