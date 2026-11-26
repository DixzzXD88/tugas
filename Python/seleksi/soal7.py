print("1. Es teh   | Rp5.000")
print("2. Es jeruk | Rp7.000")
print("3. Kopi     | Rp8.000")
print("4. Susu     | Rp6.000")

x = int(input("Masukkan pilihan : "))

match x:
    case 1:
      print("Es Teh | Rp5.000")
    case 2:
      print("Es Jeruk | Rp7.000")
    case 3:
      print("Kopi | Rp8.000")
    case 4:
      print("Susu | Rp6.000")
    case _:
      print("Menu tidak tersedia")