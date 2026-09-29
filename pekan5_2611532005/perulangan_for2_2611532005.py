# Buat file dengan nama perulangan_for2_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2005 = int(input("Masukkan jumlah perulangan: "))
print("Perulangan ke-0 sampai ke-", ulang_2005-1)
for i_2005 in range(ulang_2005):
    print(i_2005, end=" ")
print()
print("Perulangan ke-1 sampai ke-", ulang_2005)
for i_2005 in range(1,ulang_2005+1):
    print(i_2005, end=" ")