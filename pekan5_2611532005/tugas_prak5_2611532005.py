# Buatlah program menggunakan perulangan for

tinggi_2005 = int(input("Masukkan tinggi segitiga: "))

for a_2005 in range(1, tinggi_2005 + 1):
    for b_2005 in range(tinggi_2005 - a_2005):
        print(" ", end="")
    for c_2005 in range(a_2005):
        print("*", end=" ")
    print()