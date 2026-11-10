password = "tai"
x = 1

while x <= 3:
    pw = input("Masukkan password: ")
    
    if pw == password:
        print("Login berhasil!")
        break
    else:
        if x == 3:
            print("Akun terkunci!")
        else:
            print("Password salah, coba lagi.")
        x += 1

# =================

harga_sepeda = 1500000
tabungan = 0
minggu = 0

while tabungan < harga_sepeda:
    minggu += 1
    tabungan += 100000
    print(f"Minggu ke-{minggu}: Rp{tabungan:,}".replace(",", "."))

print(f"Andi butuh {minggu} minggu untuk membeli sepeda.")
