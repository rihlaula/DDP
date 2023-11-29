#1
hasil_akhir = [
    {'nama':'Reza', 'nilai':70},
    {'nama':'Ciut', 'nilai':63},
    {'nama':'Dian', 'nilai':80},
    {'nama':'Badu', 'nilai':40}
]

def predikatLulus(data):
#menggunakan list untuk mengambil nama dari hasil_akhir
#yang memiliki nilai lebih dari 65
 lulus = [mahasiswa['nama']
    for mahasiswa in data 
    if mahasiswa ['nilai'] > 65] 
 return lulus

#memanggil fungsi lulus untuk memmberikan predikat lulus
#pada nama yang memiliki nilai lebih dari 65
hasil = predikatLulus(hasil_akhir)
print('siswa yang lulus adalah: ', hasil)

#2
buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def list_buah(buah):
 list_terbalik = []

 for i in range(len(buah)-1, -1, -1):
    list_terbalik.append(buah[i])
 return list_terbalik

hasil = list_buah(buah)
print('hasil adalah:', hasil)

#3
list_buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def duplikasi(list_buah):
  list_duplikasi = []

  for buah2 in list_buah:
    list_duplikasi.append (buah2)
    list_duplikasi.append (buah2)
  return list_duplikasi

hasil_duplikasi = duplikasi(list_buah)
print('hasil duplikasi adalah:', hasil_duplikasi )
  
#4
nama = "NurulFikri"

def konsonan (nama):
    konsonan = ""
    for i in nama :
        if i not in "aiueo":
            konsonan += i
    return konsonan

hasil3 = konsonan(nama)
print('huruf konsonan dari Nurul Fikri =', hasil3)

  
