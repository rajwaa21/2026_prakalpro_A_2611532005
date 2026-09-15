# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("========================================")
print("1. OPERATOR KEANGGOTAAN")
print("========================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_2005 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_2005 = [int(angka.strip()) for angka in input_data_2005.split(",")]

nilai_dicari_2005 = int(input("Masukkan nilai yang ingin dicari: "))    

# Operator in
hasil_2005 = nilai_dicari_2005 in data_2005
print("\nOperator keanggotaan (in)")
print(nilai_dicari_2005, "in data =", hasil_2005)

# Operator not in
hasil_2005 = nilai_dicari_2005 not in data_2005
print("\nOperator keanggotaan (not in)")
print(nilai_dicari_2005, "not in data =", hasil_2005)


print("\n========================================")
print("2. OPERATOR IDENTITAS")  
print("========================================")

# objek1 menggunakan list dari input pengguna
objek1_2005 = data_2005

# objek2 menggunakan list yang sama dengan objek1
objek2_2005 = objek1_2005

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_2005 = data_2005.copy()

print("objek1_2005 =", objek1_2005)
print("objek2_2005 =", objek2_2005)
print("objek3_2005 =", objek3_2005)

# Operator is
hasil_2005 = objek1_2005 is objek2_2005
print("\nOperator identitas IS")
print("objek1_2005 is objek2_2005 =", hasil_2005)

# Operator is not
hasil_2005 = objek1_2005 is not objek3_2005
print("\nOperator identitas IS NOT")
print("objek1_2005 is not objek3_2005 =", hasil_2005)

# Membandingkan identitas dan nilai
print("\nMembandingkan identitas dan nilai")
print("objek1_2005 is objek3_2005:", objek1_2005 is objek3_2005)
print("objek1_2005 == objek3_2005:", objek1_2005 == objek3_2005)