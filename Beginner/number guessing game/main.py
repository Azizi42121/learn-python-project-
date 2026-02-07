# game tebak angka
import random

print("Game Tebak Angka")
angka_asli = random.randint(1,10)

print("rentang angka 1-10")
print("kamu hanya bisa 3 kali menebak")

i = 0
while True:
    angka_tebakan = int(input("silahkan berikan angka tebakan anda: "))

    if angka_tebakan == angka_asli:
        print(f"selamat tebakanmu benar, angkanya adalah {angka_asli}")
        break
    elif angka_tebakan < angka_asli:
        print("tebakanmu lebih kecil daripada angka aslinya")
        i += 1
    elif angka_tebakan > angka_asli:
        print("tebakanmu lebih besar daripada angka aslinya")
        i += 1

    if i == 3:
        print("kesempatan habis, kamu kalah")
        print(f"angkanya adalah {angka_asli}")
        break