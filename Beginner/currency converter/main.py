''' mini project : Currency Convereter '''
import os
# fungsi
# untuk mata uang yang nilainya lebih rendah
def uang_rendah(higher,lower):
    hasil_konversi = lower / higher
    return hasil_konversi

# untuk mata uang yang lebih tinggi
def uang_tinggi(higher,lower):
    hasil_konversi = higher * lower
    return hasil_konversi

# format penulisan nominal uang
def formatted_nominal(angka):
    return f"{angka:,.2f}".replace(",","TEMP").replace(".",",").replace("TEMP",".")

while True:
    # pembuka program
    os.system('cls')
    print(30*'=')
    print('Program Konversi Mata Uang')
    print(30*'=')

    # tampilan program
    print("\nSilahkan masukan mata uang yang ingin dikonversikan\n")
    mata_uang1 = str(input('dari:\t'))
    mata_uang2 = str(input('ke:\t'))
    nilai_uang = float(input('masukan nilai uang: '))

    match mata_uang1:
        case 'rupiah':
            match mata_uang2:
                case 'euro':
                    nilai_konversi = uang_rendah(19900,nilai_uang)
                    print(f'hasil konversi = {formatted_nominal(nilai_konversi)}')
                case 'dollar':
                    nilai_konversi = uang_rendah(16252,nilai_uang)
                    print(f'hasil konversi = {formatted_nominal(nilai_konversi)}')
                case 'yen':
                    nilai_konversi = uang_rendah(106,nilai_uang)
                    print(f'hasil dikonversi = {formatted_nominal(nilai_konversi)}')
                case 'won':
                    nilai_konversi = uang_rendah(11.55,nilai_uang)
                    print(f'hasil dikoversi = {formatted_nominal(nilai_konversi)}')
                case _:
                    print('input mata uang anda salah atau belum ada di dalam program, mohon untuk mengulangi')
        case 'euro':
            match mata_uang2:
                case 'rupiah':
                    nilai_konversi = uang_tinggi(19900,nilai_uang)
                    print(f'hasil dikoversi = {formatted_nominal(nilai_konversi)}')
                case 'dollar':
                    nilai_konversi = uang_tinggi(1.16,nilai_uang)
                    print(f'hasil dikonversi = {formatted_nominal(nilai_konversi)}')
                case 'yen':
                    nilai_konversi = uang_tinggi(1831.51,nilai_uang)
                    print(f'hasil dikonversi = {formatted_nominal(nilai_konversi)}')
                case 'won':
                    nilai_konversi = uang_tinggi(1699.11,nilai_uang)
                    print(f'hasil dikonversi = {formatted_nominal(nilai_konversi)}')
                case _:
                    print('input mata uang anda salah atau belum ada di dalam program, mohon untuk mengulangi')
        case 'dollar':
            match mata_uang2:
                case 'rupiah':
                    nilai_konversi = uang_tinggi(16252,nilai_uang)
                    print(f'hasil dikonversi = {formatted_nominal(nilai_konversi)}')
                case 'euro':
                    nilai_konversi = uang_rendah(1.16,nilai_uang)
                    print(f'hasil dikonversi = {formatted_nominal(nilai_konversi)}')
                case 'won':
                    nilai_konversi = uang_tinggi(1459.56,nilai_uang)
                    print(f'hasil dikonversi = {formatted_nominal(nilai_konversi)}')
                case 'yen':
                    nilai_konversi = uang_tinggi(157.57,nilai_uang)
                    print(f'hasil dikonversi {formatted_nominal(nilai_konversi)}')
                case _:
                    print('input mata uang anda salah atau belum ada di dalam program, mohon untuk mengulangi')
        case 'yen':
            match mata_uang2:
                case 'rupiah':
                    nilai_konversi = uang_tinggi(106.88,nilai_uang)
                    print(f'hasil dikonversi = {formatted_nominal(nilai_konversi)}')
                case 'euro':
                    nilai_konversi = uang_rendah(183.48,nilai_uang)
                    print(f'hasil dikonversi = {formatted_nominal(nilai_konversi)}')
                case 'dollar':
                    nilai_konversi = uang_rendah(157.57,nilai_uang)
                    print(f'hasil dikonversi = {formatted_nominal(nilai_konversi)}')
                case 'won':
                    nilai_konversi = uang_tinggi(9.26,nilai_uang)
                    print(f'hasil dikonversi = {formatted_nominal(nilai_konversi)}')
                case _:
                    print('input mata uang anda salah atau belum ada di dalam program, mohon untuk mengulangi')
        case 'won':
            match mata_uang2:
                case 'rupiah':
                    nilai_konversi = uang_tinggi(11.55,nilai_uang)
                    print(f'hasil dikonversi = {formatted_nominal(nilai_konversi)}')
                case 'euro':
                    nilai_konversi = uang_rendah(1699.11,nilai_uang)
                    print(f'hasil dikonversi = {formatted_nominal(nilai_konversi)}')
                case 'dollar':
                    nilai_konversi = uang_rendah(1459.56,nilai_uang)
                    print(f'hasil dikonversi = {formatted_nominal(nilai_konversi)}')
                case 'yen':
                    nilai_konversi = uang_rendah(9.26,nilai_uang)
                    print(f'hasil dikonversi = {formatted_nominal(nilai_konversi)}')
                case _:
                    print('input mata uang anda salah atau belum ada di dalam program, mohon untuk mengulangi')
        case _:
            print('input mata uang anda salah atau belum ada di dalam program, mohon untuk mengulangi')
    
    option_user = input('apakah anda ingin melanjutkannya (y/n): ')
    if option_user == 'n':
        break