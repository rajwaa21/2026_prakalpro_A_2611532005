print ("\n=== SISTEM TRANSAKSI TOKO ===")

nama_2005 = input("Masukkan Nama Pelanggan: ")
status_2005 = input("Masukkan Status Pelanggan (member/nonmember): ")
total_belanja_2005 = int(input("Masukkan Total Belanja : "))
jumlah_barang_2005 = int(input("Masukkan Jumlah Barang : "))
promo_2005 = input("Masukkan Kode Promo : ")

print("\n=== DATA TRANSAKSI ===")
print("Nama Pelanggan                     : ",nama_2005)
print("Status Pelanggan (member/nonmember): ", status_2005)
print(f"Total Belanja                      :  Rp{total_belanja_2005}")
print("Jumlah Barang                      : ", jumlah_barang_2005)
print("Kode Promo                         : ", promo_2005)

kode_promo_2005 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

syarat_total_2005 = total_belanja_2005 >=200000
syarat_jumlah_barang_2005 = jumlah_barang_2005 >=3
valid_status_2005 = status_2005 == "member"
valid_promo_2005 = promo_2005 in kode_promo_2005 

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000                : {syarat_total_2005}") 
print(f"Jumlah Barang >= 3                 : {syarat_jumlah_barang_2005}")
print(f"Status Member                      : {valid_status_2005}")
print(f"Kode Promo Tersedia                : {valid_promo_2005}")
print(f"Mendapatkan Diskon                 : {syarat_jumlah_barang_2005 or syarat_total_2005}")
print(f"Mendapatkan Promo                  : {valid_promo_2005}")

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                             : Rp{int(0.10 * total_belanja_2005)}")
print(f"Total Pembayaran                   : Rp{int(total_belanja_2005 - 0.10 * total_belanja_2005)}")
print(f"Rata-rata Harga Barang             : Rp{int((total_belanja_2005 - 0.10 * total_belanja_2005) // jumlah_barang_2005)}")

print("\n--- HAK AKSES PELANGGAN ---")
print("Kode Hak Akses         : ...")
print(f"Member Access          : {status_2005 == 'member'}")
print(f"Promo Access           : {promo_2005 in kode_promo_2005}")
print("Free Shipping Access   : ...")

print("\n=== OPERASI BITWISE ===")

print("\n=== Kode Status Transaksi ===")

# Kondisi
# 0001 = Pelanggan merupakan member
# 0010 = Total belanja >= Rp 200000
# 0100 = Jumlah barang >= 3
# 1000 = Kode promo tersedia

kode_transaksi_2005 = int(valid_status_2005) << 0 | int(syarat_total_2005) << 1 | int(syarat_jumlah_barang_2005) << 2 | int(valid_promo_2005) << 3
kode_referensi_2005 = int(valid_status_2005) << 0 | int(syarat_total_2005) << 1 | int(valid_promo_2005) << 3

print(f"{format(int(valid_status_2005) << 0, '04b')} | {format(int(syarat_total_2005) << 1, '04b')} | {format(int(syarat_jumlah_barang_2005) << 2, '04b')} | {format(int(valid_promo_2005) << 3, '04b')}")
print(f"Kode Biner   : {format(kode_transaksi_2005, '04b')}")
print(f"Kode Desimal : {kode_transaksi_2005}")

print("\n=== Pemeriksaan Status ===")

print("\nCek Member")
print(f"{format(kode_transaksi_2005, '04b')} & {format(int(valid_status_2005) << 0, '04b')}")
print(f"Hasil Biner  : {format((kode_transaksi_2005) & int(valid_status_2005) << 0, '04b')}")
print(f"Hasil Desimal: {(kode_transaksi_2005) & int(valid_status_2005) << 0}")

print("\nCek Promo")
print(f"{format(kode_transaksi_2005, '04b')} & {format(int(valid_promo_2005) << 3, '04b')}")
print(f"Hasil Biner  : {format((kode_transaksi_2005) & int(valid_promo_2005) << 3, '04b')}")
print(f"Hasil Desimal: {(kode_transaksi_2005) & int(valid_promo_2005) << 3}")

print("\n=== Perbandingan Status ===")
print(f"Kode Transaksi: {format(kode_transaksi_2005, '04b')}")
print(f"Kode Referensi: {format(kode_referensi_2005, '04b')}")
print(f"{format(kode_transaksi_2005, '04b')} ^ {format(kode_referensi_2005, '04b')}")
print(f"Hasil Biner  : {format((kode_transaksi_2005) ^ (kode_referensi_2005), '04b')}")
print(f"Hasil Desimal: {(kode_transaksi_2005) ^ (kode_referensi_2005)}")

print("\n=== Shift ===")
print(f"{format(kode_transaksi_2005, '04b')} << 1")
print(f"Hasil Biner  : {format((kode_transaksi_2005) << 1, '04b')}")
print(f"Hasil Desimal: {(kode_transaksi_2005) << 1}")

print("=== SELESAI ===")