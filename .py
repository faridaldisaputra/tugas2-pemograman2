nama = input("Masukkan nama: ")
npm = input("Masukkan NPM: ")
umur = input("Masukkan umur: ")
tinggi = input("Masukkan tinggi: ")
prodi = input("Masukkan prodi: ")

tugas = int(input("Masukkan nilai tugas: "))
uts = int(input("Masukkan nilai UTS: "))
uas = int(input("Masukkan nilai UAS: "))

nilai_akhir = (tugas + uts + uas) / 3

print("\n===== DATA DIRI =====")
print("Nama         :", nama)
print("NPM          :", npm)
print("Umur         :", umur)
print("Tinggi       :", tinggi, "cm")
print("Prodi        :", prodi)
print("Nilai Tugas  :", tugas)
print("Nilai UTS    :", uts)
print("Nilai UAS    :", uas)
print("Nilai Akhir  :", nilai_akhir)

if nilai_akhir >= 75:
    print("Keterangan   : Selamat anda lulus")
else:
    print("Keterangan   : Maaf anda tidak lulus")