print("1. Member")
print("2. Non member")
kategori = int(input("Jenis pelanggan : "))
belanja = int(input("Masukkan total belanja : Rp"))

match kategori:
    case 1:
      if belanja >= 100000:
        print("Selamat anda mendapatkan diskon 10%") 
      else:
        print("Anda idak mendapatkan diskon")
    case 2:
      if belanja >= 100000:
        print("Selamat anda mendapatkan diskon 5%") 
      else:
        print("Anda tidak mendapatkan diskon")
    case _:
      print("Kategori tidak valid")