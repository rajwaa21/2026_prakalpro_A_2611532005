# BACA height 
# UNTUK row DARI 1 SAMPAI height     
#     UNTUK column DARI 1 SAMPAI row         
#         TAMPILKAN column DAN satu spasi, TANPA pindah baris     
#     PINDAH BARIS 

height = int(input("Enter height: "))

for row in range(1, height + 1):
    for column in range(1, row + 1):
        print(column, end=" ")
    print()