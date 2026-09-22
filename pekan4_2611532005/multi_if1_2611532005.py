# Buat file dengan nama multi_if1_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_2005 = int(input("Input umur anda: "))
sim_2005 = input("Apakah Anda Sudah Punya SIM C (y/t): ") [0]

if umur_2005 >= 17 and sim_2005 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")

if umur_2005 >= 17 and sim_2005 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

if umur_2005 < 17 and sim_2005 == 'y':
    print("Anda Belum Cukup Umur punya SIM")

if umur_2005 < 17 and sim_2005 != 'y':
    print("Anda Belum Cukup Umur bawa motor")