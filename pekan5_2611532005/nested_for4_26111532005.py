# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_2005 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2005 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_2005 = tinggi_2005
    c_2005 = a_2005
    lebar_2005 = (2 * tinggi_2005) - 2

    for i_2005 in range(1, tinggi_2005 + 1):
        b_2005 = c_2005 + 1

        for j_2005 in range(1, lebar_2005 + 1):

            # Baris atas dan bawah
            if i_2005 == 1 or i_2005 == tinggi_2005:
                if j_2005 == 1 or j_2005 == lebar_2005:
                    print("#", end="")
                else:
                    print("=", end="")

            # Baris isi
            else:
                if j_2005 == 1 or j_2005 == lebar_2005:
                    print("|", end="")
                else:
                    if j_2005 == c_2005:
                        print("<", end="")
                    elif j_2005 == b_2005:
                        print(">", end="")
                    elif j_2005 == (lebar_2005 - c_2005):
                        print("<", end="")
                    elif j_2005 == (lebar_2005 - c_2005 + 1):
                        print(">", end="")
                    elif j_2005 > b_2005 and j_2005 < (lebar_2005 - c_2005):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli java
        a_2005 -= 2

        if a_2005 <= 0:
            c_2005 = (-a_2005 + 2)
        else:
            c_2005 = a_2005