print("Menu makanan :")
print("1.Nasgor goreng")
print("2.Kwetiau")

pilihan = input("Masukkan pilihan makanan : ")

match pilihan:
    case "1":
        print("Nasgor goreng")
        print("Harga Rp67.000")
    case "2":
        print("Kwetiau")
        print("Harga Rp676.000")
      
    case _:
        print("makanannya udah basi")
