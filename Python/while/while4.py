from getpass import getpass
print("=== PROGRAM KUIS ===")
pertanyaan = input("Masukkan pertanyaan: ")
kunci_jawaban = getpass("Masukkan kunci jawaban (tersembunyi): ")

print("\n=== MULAI KUIS ===")
percobaan = 0
batas_percobaan = 3

while percobaan < batas_percobaan:
    print("\nPertanyaan:", pertanyaan)
    jawaban = input("Jawaban kamu: ")

    if jawaban.lower() == kunci_jawaban.lower():
        print("Jawaban BENAR!")
        print("Selamat! Kamu berhasil menjawab.")
        break
    else:
        percobaan += 1
        sisa = batas_percobaan - percobaan

        print("Jawaban SALAH!")

        if sisa > 0:
            print("Kesempatan tersisa:", sisa)
        else:
            print("Kamu GAGAL! Kesempatan habis.")
print(f"\nJawaban Adalah {kunci_jawaban}")
print("\n=== PROGRAM SELESAI ===")