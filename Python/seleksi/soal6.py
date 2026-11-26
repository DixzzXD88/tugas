bulan = int(input("Masukkan bulan ke -"))

match bulan:
    case 1:
      print("Januari")
    case 2:
      print("Februari")
    case 3:
      print("Maret")
    case 4:
      print("April")
    case 5:
      print("Mei")
    case 6:
      print("Juni")
    case _:
      print("Bulan tidak tersedia")