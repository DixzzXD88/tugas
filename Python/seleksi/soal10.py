usia = int(input("Masukkan usia : "))

if usia >= 17:
    print("1. Horror")
    print("2. Komedi")
    print("3. Keluarga")
    print("4. Aksi")
    genre = int(input("Masukkan pilihan genre : "))
    match genre:
        case 1:
            print("1. Horror Indonesia")
            print("2. Horror Luar Negeri")
            subgenre = int(input("Masukkan pilihan subgenre : "))
            match subgenre:
                case 1:
                  print("Selamat Menyaksikan Film Horror Indonesia")
                case 2:
                  print("Selamat Menyaksikan Film Horror Luar Negeri")
                case _:
                  print("Pilihan Subgenre tidak valid")
        case 2:
            print("1. Komedi Indonesia")
            print("2. komedi Luar Negeri")
            subgenre = int(input("Masukkan pilihan subgenre : "))
            match subgenre:
                case 1:
                  print("Selamat Menyaksikan Film komedi Indonesia")
                case 2:
                  print("Selamat Menyaksikan Film Komedi Luar Negeri")
                case _:
                  print("Pilihan Subgenre tidak valid")
        case 3:
            print("1. Keluarga Indonesia")
            print("2. keluarga Luar Negeri")
            subgenre = int(input("Masukkan pilihan subgenre : "))
            match subgenre:
                case 1:
                  print("Selamat Menyaksikan Film Keluarga Indonesia")
                case 2:
                  print("Selamat Menyaksikan Film Keluarga Luar Negeri")
                case _:
                  print("Pilihan Subgenre tidak valid")
        case 4:
            print("1. Aksi Hollywood")
            print("2. Aksi Indonesia")
            print("3. Aksi Bollywood")
            subgenre = int(input("Masukkan pilihan subgenre : "))
            match subgenre:
                case 1:
                  print("Selamat Menyaksikan Film Aksi Indonesia")
                case 2:
                  print("Selamat Menyaksikan Film Aksi Luar Negeri")
                case _:
                  print("Pilihan Subgenre tidak valid")
        case _:
          print("Pilihan genre tidak valid")

else:
    print("1. 2 Dimensi")
    print("2. 3 Dimensi")
    genre = int(input("Masukkan pilihan genre : "))
    match genre:
        case 1:
            print("1. Naruto")
            print("2. One Piece")
            subgenre = int(input("Masukkan pilihan subgenre : "))
            match subgenre:
                case 1:
                  print("Selamat Menyaksikan Film Naruto")
                case 2:
                  print("Selamat Menyaksikan Film One Piece")
                case _:
                  print("Pilihan Subgenre tidak valid")
        case 2:
            print("1. Nemo")
            print("2. Kungfu Panda")
            subgenre = int(input("Masukkan pilihan subgenre : "))
            match subgenre:
                case 1:
                  print("Selamat Menyaksikan Film Nemo")
                case 2:
                  print("Selamat Menyaksikan Film Kungfu Panda")
                case _:
                  print("Pilihan Subgenre tidak valid")
        case _:
          print("Pilihan genre tidak valid")