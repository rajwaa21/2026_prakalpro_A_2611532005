# Buat file dengan nama perulangan_for3_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2005 = int(input("Masukkan jumlah perulangan: "))

jumlah_2005 = 0
for i_2005 in range(1, ulang_2005 + 1):
    print(i_2005, end=" ")
    jumlah_2005 = jumlah_2005 + i_2005

    if i_2005 < ulang_2005:
        print(" + ", end="")
    else:
        print(" = ", jumlah_2005, end="")
print()
print("Jumlah =", jumlah_2005)