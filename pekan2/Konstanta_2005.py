# Buat file dengan nama konstanta_NIM.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: jari_1234

from typing import Final
PI: Final = 3.14
print ("pi: %f" % (PI))
jari_2005 = float(input('Masukkan nilai jari-jari:'))
luas_2005 = PI * jari_2005 * jari_2005
print("luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2005, luas_2005))
