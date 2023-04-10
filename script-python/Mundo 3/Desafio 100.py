from random import randint
from time import sleep
numeros = []
def sorteio():
    for cont in range(0, 5):
        numeros.append(randint(0, 10))
    print('Sorteando 5 valores da lista: ', end='')
    for c in numeros:
        print(f'{c}', end=' ')
        sleep(0.5)
    print('PRONTO!!')


def somaPar():
    somapa = 0
    for c in numeros:
        if c % 2 == 0:
            somapa += c
    print(f'Somando os valores {numeros}, Temos {somapa}')


sorteio()
somaPar()

