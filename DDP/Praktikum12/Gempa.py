class gempa:
    #atribut class
    lokasi = ''
    skala = 0

    #construktor
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if (self.skala < 2):
             ket= "Maka dampak gempa tidak berasa"
        elif (self.skala < 2 and self.skala >4):
             ket= "Maka dampak gempa bangunan Retak-retak"
        elif (self.skala < 4 and self.skala >6):
             ket= "Maka dampak gempa sangat roboh"
        else:
            ket= "maka dampak gempa bangunan roboh dan berpotensi tsunami"
        
        print(f'Lokasi:{self.lokasi}')
        print(f'Skala:{self.skala}')
        print(f'Keterangan:{ket}')


    

          
   