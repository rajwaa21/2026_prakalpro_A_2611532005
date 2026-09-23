print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

nama_2005 = input("Masukkan Nama Pengunjung : ")
umur_2005 = int(input("Input umur anda : "))
sim_2005 = input("Apakah Anda Sudah Punya SIM C (y/t) : ").strip().lower()

# Pilihan paket wahana:
# case 1: "Wahana Safari Rimba" | Harga Satuan: Rp 50.000
# case 2: "Wahana Arung Jeram" | Harga Satuan: Rp 75.000
# case 3: "Wahana Motor ATV Ekstrim" | Harga Satuan: Rp 120.000
# case 4: "Wahana Roller Coaster Kilat" | Harga Satuan: Rp 100.000
# case 5: "Wahana All-Access VIP" | Harga Satuan: Rp 220.000
# case _: Cetak pesan "Paket wahana tidak valid!" dan hentikan eksekusi transaksi.

print("\nPilihan Paket Wahana (1-5):")
print("1. Safari Rimba          (Rp 50,000)")
print("2. Arung Jeram           (Rp 75,000)")
print("3. Motor ATV Ekstrim     (Rp 120,000)")
print("4. Roller Coaster Kilat  (Rp 100,000)")
print("5. All-Access VIP        (Rp 220,000)")

paket_2005 = int(input("Masukkan nomor paket (1-5) : "))

match paket_2005:
    case 1:
        wahana_2005 = "Safari Rimba"
        harga_satuan_2005 = 50000
    case 2:
        wahana_2005 = "Arung Jeram"
        harga_satuan_2005 = 75000
    case 3:
        wahana_2005 = "Motor ATV Ekstrim"
        harga_satuan_2005 = 120000
    case 4:
        wahana_2005 = "Roller Coaster Kilat"
        harga_satuan_2005 = 100000
    case 5:
        wahana_2005 = "All-Access VIP"
        harga_satuan_2005 = 220000
    case _:
        print("Paket wahana tidak valid!")
        exit()

jumlah_tiket_2005 = int(input("Masukkan jumlah tiket : "))

member_2005 = input("Apakah Anda member? (y/t) : ").strip().lower()
kode_promo_2005 = input("Apakah kode promo valid? (y/t) : ").strip().lower()

print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

# Khusus untuk Paket 3 (Motor ATV Ekstrim), evaluasi izin pengendara:
# if umur >= 17 and sim == 'y', Cetak: "Anda sudah dewasa dan boleh mengendarai ATV sendiri."
# elif umur >= 17 and sim != 'y', Cetak: "Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur)."
# elif umur < 17 and sim == 'y, Cetak: "Identitas tidak valid: Belum cukup umur memiliki SIM."
# else:, Cetak: "Anda belum cukup umur dan tidak boleh bawa motor ATV."

if paket_2005 == 3:
    if umur_2005 >= 17 and sim_2005 == 'y':
        print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
    elif umur_2005 >= 17 and sim_2005 != 'y':
        print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
    elif umur_2005 < 17 and sim_2005 == 'y':
        print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
    else:
        print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")

# Untuk paket selain 3, gunakan if-else sederhana untuk mengecek apakah umur >= 10 tahun).
else:
    if umur_2005 >= 10:
            print("Status Akses: Anda memenuhi syarat umur untuk", wahana_2005)
    else:
            print("Status Akses: Anda belum memenuhi syarat umur untuk", wahana_2005)

# Hitung subtotal = harga_satuan * jumlah_tiket.
# if subtotal >= 200000: total_diskon_persen += 10 (Diskon Belanja Besar)
# if is_member in ['y', 'ya']: total_diskon_persen += 5 (Diskon Member)
# if kode_promo_valid in ['y', 'ya']: total_diskon_persen += 15 (Diskon Voucher Promo)
# if jumlah_tiket >= 5: total_diskon_persen += 5 (Diskon Tambahan Rombongan)

subtotal_2005 = harga_satuan_2005 * jumlah_tiket_2005
diskon_2005 = 0

if subtotal_2005 >= 200000: 
    diskon_2005 += 10 # Diskon Belanja Besar
if member_2005 in ['y', 'ya']:
    diskon_2005 += 5 # Diskon Member
if kode_promo_2005 in ['y', 'ya']:
    diskon_2005 += 15 # Diskon Voucher Promo
if jumlah_tiket_2005 >= 5:
    diskon_2005 += 5 # Diskon Tambahan Rombongan

nominal_diskon_2005 = subtotal_2005 * (diskon_2005 / 100)
total_bayar_2005 = subtotal_2005 - nominal_diskon_2005

print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {subtotal_2005:,.0f}")
print(f"Total Diskon     : {diskon_2005}% (Rp {nominal_diskon_2005:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_2005:,.0f}")

if total_bayar_2005 > 300000:
    print("Catatan Layanan  : Selamat! Anda berhak mendapatkan Souvenir Gratis.")
else:
    print("Catatan Layanan  : Terima kasih telah berkunjung.")

print("Program Selesai")