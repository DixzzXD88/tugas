from getpass import getpass

print("=== PERMAINAN TEBAK ANGKA ===")
angka_rahasia = int(getpass("Masukkan angka rahasia (1-10): "))

percobaan = 0
batas_percobaan = 3
print("\n=== MULAI PERMAINAN ===")

while percobaan < batas_percobaan:
    tebakan = int(input("Tebak angka (1-10): "))

    if tebakan == angka_rahasia:
        print("Selamat! Tebakan kamu benar.")
        break

    elif tebakan < angka_rahasia:
        print("Terlalu kecil!")

    else:
        print("Terlalu besar!")

    percobaan += 1

    sisa = batas_percobaan - percobaan

    if sisa > 0:
        print(f"Kesempatan tersisa: {sisa}")
    else:
        print("Kamu gagal! Kesempatan habis.")

print(f"\nAngka rahasianya adalah : {angka_rahasia}")
print("\n=== PERMAINAN SELESAI ===")