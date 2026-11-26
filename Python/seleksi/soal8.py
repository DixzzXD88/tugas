print("1. Teori")
print("2. Praktik")
kategori = int(input("Pilih kategori ujian : "))

match kategori:
    case 1:
      nilai = int(input("Masukkan nilai teori : "))
      if nilai >= 75:
        print("Selamat, Anda Lulus") 
      else:
        print("Maaf, Anda Tidak Lulus")
    case 2:
      nilai = int(input("Masukkan nilai praktik : "))
      if nilai >= 75:
        print("Selamat, Anda Lulus") 
      else:
        print("Maaf, Anda Tidak Lulus")
    case _:
        print("Kategori ujian tidak valid")