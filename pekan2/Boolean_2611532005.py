# deklarasi variabel dengan tipe data boolean
is_lulus_2005 = True
is_cumlaude_2005 = True

#menggunakan boolean
nilai_2005 = 85
batas_lulus_2005 = 75

# menentukan nilai boolean dari kondisi
status_kelulusan_2005 = nilai_2005 >= batas_lulus_2005 #hasilnya akan true

print("=== Check Status Kelulusan ===")
print("Nilai_2005:", nilai_2005)
print("Apakah lulus?:", status_kelulusan_2005)
if is_lulus_2005 and is_cumlaude_2005:
    print("Selamat, Anda lulus dengan predikat Cumlaude!")