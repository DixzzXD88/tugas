import os

clear = lambda: os.system('cls')

name = input("Nama : ")
umur = input("Umur : ")
kelas = input("Kelas : ")
jurusan = input("Jurusan : ")
alamat = input("Alamat : ")
email = input("E-Mail : ")
phone = input("No. HP : ")

clear()
print("-_-_-_-_-_ BIODATA _-_-_-_-_-")
print(f"Nama   : {name}")
print(f"Alamat : {alamat}")
print(f"Umur   : {umur} tahun")
print(f"Kelas  : {kelas}")
print(f"E-Mail : {email}")
print(f"No. HP : {phone}")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
