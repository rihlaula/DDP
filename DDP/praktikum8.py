#profil
def say(nama, alamat, gender, umur, hoby):
    print("nama saya ", nama)
    print("tempat tinggal saya ", alamat)
    print("gender saya adalah ", gender)
    print("usia saya ", umur)
    print("hoby saya ", hoby)

say("rihlatul ula rahmat", "di depok sawangan", "perempuan", "18 tahun", "memasak")

#kelulusan
def kelulusan(nilai):
   if nilai <= 60:
       return "Gagal"
   elif 61 <= nilai <= 70:
       return "Baik"
   elif 71 <= nilai <= 80:
       return "Sangat Baik"
   elif 81 <= nilai <= 100:
       return "Istimewa"
   else:
       return "kelulusan"

print(kelulusan(60))

#nilai bilangan ganjil dari parameter
def bilangan_ganjil(n):
    for i in range(1, n+1, 2):
        print(i)

# hasil
bilangan_ganjil(100)