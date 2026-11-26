print("===== MENU MAKANAN =====")
print("1. Nasgor Goreng")
print("2. Mie Ayam")
print("3. Bakso")
print("4. Es Teh")
print("5. Jus Jeruk")
print("========================")

pilihan = int(input("Pilih menu makanan : "))

match pilihan:
    case 1:
        print("-_-_-_-_-_-_-_-")
        print("Nasgor Goreng")
        print("Rp15.000")
        print("-_-_-_-_-_-_-_-")
    case 2:
        print("-_-_-_-_-_-_-_-")
        print("Mie Ayam")
        print("Rp12.000")
        print("-_-_-_-_-_-_-_-")
    case 3:
        print("-_-_-_-_-_-_-_-")
        print("Bakso")
        print("Rp13.000")
        print("-_-_-_-_-_-_-_-")
    case 4:
        print("-_-_-_-_-_-_-_-")
        print("Es Teh")
        print("Rp5.000")
        print("-_-_-_-_-_-_-_-")
    case 5:
        print("-_-_-_-_-_-_-_-")
        print("Jus Jeruk")
        print("Rp8.000")
        print("-_-_-_-_-_-_-_-")
    case _:
        print("IQ lu dimana pruyyyy")