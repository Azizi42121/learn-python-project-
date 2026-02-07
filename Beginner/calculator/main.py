# mini project: calculator
while True:
    print('='*50)
    print('CALCULATOR')
    print('='*50)

    angka1 = int(input('angka pertama:\t\t'))
    operator = str(input('operator (*,/,+,-): \t'))
    angka2 = int(input('angka kedua:\t\t'))

    if operator == '+':
        hasil = angka1 + angka2
        print(f'hasilnya = {hasil}')
    elif operator == '-':
        hasil = angka1 - angka2
        print(f'hasilnya = {hasil}')
    elif operator == '*':
        hasil = angka1*angka2
        print(f'hasilnya = {hasil}')
    elif operator == '/':
        hasil = angka1/angka2
        print(f'hasilnya = {hasil}')

    option = input('apakah ingin melanjutkan program (y/n)? ')

    if option == 'n':
        break