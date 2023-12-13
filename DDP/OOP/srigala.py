class srigala:
    #atribut class
    nama = ''
    warna = ''
    umur = 0

    #construktor
    def __init__(self, nama, warna, umur):
        self.nama = nama
        self.warna = warna
        self.umur = umur

    # method untuk menampilkan data nya
    def data_srigala(self):
        print(f'nama srigala:{self.nama}')
        print(f'warna srigala:{self.warna}')
        print(f'umur srigala:{self.umur}')
