from random import randint
from time import sleep
lista = []
jogos = []
print('-'*30)
print('      JOGO DA MEGA SENA    ')
print('-'*30)
quant = int(input('Quantos jogos voce quer que eu sorteie? '))
cont2 = 1
while cont2 <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    cont2 += 1
print('=-'*3,end='')
print(f' SORTEANDO {quant} JOGOS ', end='')
print('=-'*3,)
sleep(1)
for i, c in enumerate(jogos):
    print(f'Jogo {i+1}: {c}')
    sleep(1)

