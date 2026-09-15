# Buat file dengan nama logika_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator logika dalam Python

# Memasukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_2005 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_2005 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print ("\nA1_2005 =", a1_2005)
print ("A2_2005 =", a2_2005)

# Konjungsi: bernilai True jika keduanya True
hasil_2005 = a1_2005 and a2_2005
print ("\nKonjungsi (AND)")
print ("A1_2005 and A2_2005 =", hasil_2005)

# Disjungsi: bernilai True jika salah satu True
hasil_2005 = a1_2005 or a2_2005
print ("\nDisjungsi (OR)")
print ("A1_2005 or A2_2005 =", hasil_2005)

# Negasi A1: membalik nilai A1
hasil_2005 = not a1_2005
print ("\nNegasi A1_2005 (NOT)")
print ("not A1_2005 =", hasil_2005)

# Negasi A2: membalik nilai A2
hasil_2005 = not a2_2005 
print ("\nNegasi A2_2005 (NOT)")
print ("not A2_2005 =", hasil_2005)

# XOR: bernilai True jika kedua nilai berbeda
hasil_2005 = a1_2005 != a2_2005
print ("\nDisjungsi Eksklusif (XOR)")
print ("A1_2005 XOR A2_2005 =", hasil_2005)