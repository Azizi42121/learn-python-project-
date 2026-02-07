# mini project url shortener

# mengimport pip yang dibutuhkan
import pyshorteners

# function
def url_shortener(url):
    long_url = url # url panjang yang ingin dipersingkat
    s = pyshorteners.Shortener() # Inisialisasi shortener (dengan Tinyurl)
    short_url =  s.tinyurl.short(long_url) # persingkat url
    return short_url

# tampilan program 
while True:
    # pembuka
    print('='*50)
    print('URL SHORTENER PROGRAM')
    print('='*50)

    # meminta url yang ingin dipersingkat
    input_user = input('masukan tautan yang ingin dipersingkat: \n')

    # proses menyingkat url
    result_short = url_shortener(input_user)

    # menampilkan url yang telah dipersingkat
    print(f'\nini tautan yang sudah dipersingkat \n {result_short}')
    print('\n','='*50)

    # pilihan untuk mengakhiri program
    option_end = input('apakah ingin mengakhiri program (y/n): ')
    print('\n\n\n')
    if option_end == 'y':
        break