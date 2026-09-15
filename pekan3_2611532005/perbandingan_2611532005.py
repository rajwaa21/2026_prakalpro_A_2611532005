# Buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_2005 = int(input("Input angka-1: "))
angka2_2005 = int(input("Input angka-2: "))

# Lebih besar dari
hasil_2005 = angka1_2005 > angka2_2005
print("\nOperator lebih besar dari")
print("angka1_2005 > angka2_2005", hasil_2005)

# Lebih kecil dari
hasil_2005 = angka1_2005 < angka2_2005
print("\nOperator lebih kecil dari")
print("angka1_2005 < angka2_2005", hasil_2005)

# Lebih besar dari atau sama dengan
hasil_2005 = angka1_2005 >= angka2_2005
print("\nOperator lebih besar dari atau sama dengan")
print("angka1_2005 >= angka2_2005", hasil_2005)

# Lebih kecil dari atau sama dengan
hasil_2005 = angka1_2005 <= angka2_2005
print("\nOperator lebih kecil dari atau sama dengan")
print("angka1_2005 <= angka2_2005", hasil_2005)

# Sama dengan
hasil_2005 = angka1_2005 == angka2_2005
print("\nOperator sama dengan")
print("angka1_2005 == angka2_2005 =", hasil_2005)

# Tidak sama dengan
hasil_2005 = angka1_2005 != angka2_2005
print("\nOperator tidak sama dengan")
print("angka1_2005 != angka2_2005 =", hasil_2005)

# Tambahan: perbandingan berantai dalam Python
hasil_2005 = 0 < angka1_2005 < 100
print("\nPerbandingan berantai")
print("0 < angka1_2005 < 100 =", hasil_2005)

hasil_2005 = 0 < angka2_2005 < 100
print("0 < angka2_2005 < 100 =", hasil_2005)