# game gunting batu kertas
import random

print("GUNTING BATU KERTAS")

pilihan = ['Gunting','Batu','Kertas']

x = 'jalan'
while x == 'jalan':
    # pilihan komputer
    komputer = random.choice(pilihan)

    # pilihan user
    manusia = input("Masukkan pilihan (Gunting/Batu/Kertas): ")

    # proses koreksi pilihan manusia
    if manusia in ['gunting','batu','kertas']:
        manusia = manusia.capitalize()

    # proses menentukan menang atau kalah
    if komputer == manusia:
        print("Hasil = Seri")
        print(f"Manusia ({manusia}) dan Komputer ({komputer})")
    elif (manusia == "Gunting" and komputer == "Kertas") or (manusia == "Batu" and komputer == "Gunting") or (manusia == "Kertas" and komputer == "Batu"):
        print("Hasil : Kamu menang!!")
        print(f"Manusia ({manusia}) dan Komputer ({komputer})")
    else:
        print("Hasil : Kamu Kalah!!")
        print(f"Manusia ({manusia}) dan Komputer ({komputer})")

    # piihan apakah ingin melanjutkan program atau tidak
    islanjut = input("apakah ingin bermain lagi? (y/n): ")

    if islanjut == "n":
        x = 'tidak jalan'

    