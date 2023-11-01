#
a = 'saya'
jajan = 50000

if (jajan <= 15000):
  keterangan = 'jajan cukup'
else:
  keterangan = 'jajan berlebih'
print(a,'jajan hari ini sebesar', jajan, keterangan  )

#
a = 'saya'
beratbadan = 57

if (beratbadan <= 57):
  keterangan = 'berat badan cukup'
else:
  keterangan = 'berat badan berlebih'
print(a,'berat badan hari ini sebesar', beratbadan, keterangan )

#
pelanggan = 'zaky'
totalbelanja =  300000

if (totalbelanja == 200000):
  ket = 'jajan di sturback'
elif (totalbelanja >= 100000):
  ket = 'kamu irit'

print('pelanggan', pelanggan, 'total belanja anda Rp.',totalbelanja,ket)

# variabel
nama = 'Rihlatul'
prodi = 'Si03'
nim = '0110123204'
matkul = 'DDP'
nilai = 95

if (nilai >= 90):
  ket = 'maka grade nya adalah A'
elif (nilai > 80):
  ket = 'maka grade B'
elif (nilai > 70):
  ket = 'maka gradenya C'
else:
  ket = 'dibawah nilai di atas maka gradenya D'

print('Dengan nama', nama, 'dengan prodi', prodi, nim, 'telah mendapatkan grade', nilai, 'dimatkul', matkul, ket )