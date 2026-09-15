# Buat file dengan nama aritmatika_NIM.py
# Buat program untuk operator aritmatika dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input() 
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_2005 = int(input("Input angka-1: "))
angka2_2005 = int(input("Input angka-2: "))

# Penjumlahan
hasil_2005 = angka1_2005 + angka2_2005
print("\nOperator Penjumlahan")
print("Hasil =", hasil_2005)

# Pengurangan
hasil_2005 = angka1_2005 - angka2_2005
print("\nOperator Pengurangan")
print("Hasil =", hasil_2005)

# Perkalian
hasil_2005 = angka1_2005 * angka2_2005
print("\nOperator Perkalian")
print("Hasil =", hasil_2005)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_2005 != 0:
    hasil_2005 = angka1_2005 / angka2_2005
    print("\nOperator Pembagian")
    print("Hasil =", hasil_2005)

    hasil_2005 = angka1_2005 // angka2_2005
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_2005)

    hasil_2005 = angka1_2005 % angka2_2005
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_2005)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_2005 = angka1_2005 ** angka2_2005
print("\nOperator Pangkat")
print("Hasil =", hasil_2005)