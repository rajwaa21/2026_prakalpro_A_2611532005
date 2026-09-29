# Buat file dengan nama nested_for3_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2005 = int(input("Masukkan nilai batas: "))
for i_2005 in range(batas_2005+1):
    for j_2005 in range(batas_2005+1):
        print(i_2005 + j_2005, end=" ")
    print() # pindah ke baris berikutnya