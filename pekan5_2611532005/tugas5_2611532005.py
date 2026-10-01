print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

n_2005 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Border Atas:
print("#", end="")
for i_2005 in range(4 * n_2005 + 5):
    print("=", end="")
print("#")

# Jam Pasir Atas
for baris_2005 in range(n_2005, 0, -1):
    print("| ", end="")
    
    for spasi_2005 in range(2 * (n_2005 - baris_2005)):
        print(" ", end="")

    for angka_2005 in range(baris_2005, 0, -1):
        print(f"{angka_2005} ", end="")
        
    print("<*>", end="")

    for angka_2005 in range(1, baris_2005 + 1):
        print(f" {angka_2005}", end="")
        
    for spasi_2005 in range(2 * (n_2005 - baris_2005)):
        print(" ", end="")
        
    print(" |")

# Poros Titik Pusat Jam Pasir 
print("|", end="")
for spasi_2005 in range(2 * n_2005 + 1):
    print(" ", end="")
    
print("<*>", end="")

for spasi_2005 in range(2 * n_2005 + 1):
    print(" ", end="")
    
print("|")

# Jam Pasir Bawah
for baris_2005 in range(1, n_2005 + 1):
    print("| ", end="")
    
    for spasi_2005 in range(2 * (n_2005 - baris_2005)):
        print(" ", end="")

    for angka_2005 in range(baris_2005, 0, -1):
        print(f"{angka_2005} ", end="")    
        
    print("<*>", end="")

    for angka_2005 in range(1, baris_2005 + 1):
        print(f" {angka_2005}", end="") 
        
    for spasi_2005 in range(2 * (n_2005 - baris_2005)):
        print(" ", end="")
        
    print(" |")

# Border Bawah
print("#", end="")
for i_2005 in range(4 * n_2005 + 5):
    print("=", end="")
print("#")