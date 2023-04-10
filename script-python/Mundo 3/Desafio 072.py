cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
        'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
        'Dez', 'Onze', 'Doze', 'Treze', 'Catorse',
        'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito',
        'Dezenove', 'Vinte')

while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20 :
            break
        print('Digite novamente!')
    print(f'Você digitou o número {cont[num]}!')
    seg = str(input('Quer Continuar [S/N]: ')).upper().strip()[0]
    if seg in "N":
        break


