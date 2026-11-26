total = int(input("Total belanja : "))

if total >= 500000:
    d1 = total * 20/100
    diskon = total - d1
    print("Selamat kamu mendapatkan diskon sebesar 20%")
    print(f"Total yang harus dibayar adalah Rp{int(diskon)}")
elif total >= 300000:
    d1 = total * 10/100
    diskon = total - d1
    print("Selamat kamu mendapatkan diskon sebesar 10%")
    print(f"Total yang harus dibayar adalah Rp{int(diskon)}")
elif total >= 100000:
    d1 = total * 5/100
    diskon = total - d1
    print("Selamat kamu mendapatkan diskon sebesar 5%")
    print(f"Total yang harus dibayar adalah Rp{int(diskon)}")