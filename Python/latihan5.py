# PENJUMLAHAN
import os

clear = lambda: os.system('cls')
clear()

print("======= PENJUMLAHAN =======")
b1 = int(input("Masukkan bilangan 1 = "))
b2 = int(input("Masukkan bilangan 2 = "))

penjumlahan = b1 + b2
print(f"Hasil dari {b1} + {b2} = {penjumlahan}")

print("\n======= PENGURANGAN =======")
b1 = int(input("Masukkan bilangan 1 = "))
b2 = int(input("Masukkan bilangan 2 = "))

pengurangan = b1 - b2
print(f"Hasil dari {b1} - {b2} = {pengurangan}")

print("\n======= PERKALIAN =======")
b1 = int(input("Masukkan bilangan 1 = "))
b2 = int(input("Masukkan bilangan 2 = "))

perkalian = b1 * b2
print(f"Hasil dari {b1} x {b2} = {perkalian}")

print("\n======= PEMBAGIAN =======")
b1 = int(input("Masukkan bilangan 1 = "))
b2 = int(input("Masukkan bilangan 2 = "))

pembagian = b1 / b2
print(f"Hasil dari {b1} ÷ {b2} = {pembagian}")