print ("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

nama_2005 = input(str("Masukkan Nama Mahasiswa : "))
jenis_kelamin_2005 = input ("Masukkan Jenis Kelamin (L/P) : ")
umur_2005 = int(input("Masukkan Umur : "))
skor_tes_awal_2005 = float(input("Masukkan Skor Tes Awal : "))

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")

alamat_2005 = """
Komplek wisma bumi mas,
Kec. Kuranji,
Kota Padang """
id_token_sinyal = 100+3j

print("Nama Mahasiswa :", nama_2005, "|", "Tipe :", type(nama_2005))
print("Jenis Kelamin :", jenis_kelamin_2005, "|", "Tipe :", type(jenis_kelamin_2005))
print("Alamat Domisili :", alamat_2005, "|", "Tipe :", type(alamat_2005))
print("Umur :", umur_2005, "tahun", "|", "Tipe :", type(umur_2005))
print("Skor Tes Awal :", skor_tes_awal_2005, "|", "Tipe :", type (skor_tes_awal_2005))
print("ID Token Sinyal :", id_token_sinyal, "|", "Tipe :", type (id_token_sinyal))

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")

batas_2005 = 75.0

print("Batas Minimum Nilai:", batas_2005)
if skor_tes_awal_2005 >= batas_2005:
    hasil_2005 = True
else:
    hasil_2005 = False
print("Apakah dinyatakan lulus?:", hasil_2005, "|", "Tipe :", type (hasil_2005))