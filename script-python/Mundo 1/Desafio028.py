'''from random import randint
num = int(input('Digite seu número entre 0 e 5 da sorte '))
lista = (0,5)
escolha = randint(lista)
print(' O número sorteado foi {}'.format(escolha))
if escolha==num:
    print('Parabens voce foi sorteado!!!')
else:
    print('Tente novamente!!')'''
from random import randint
from time import sleep
com = randint(0,5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
print('-=-'*20)
sleep(2)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == com:
    print('PARABENS! Você pensou no mesmo número que eu pensei!')
else:
    print('TENTE OUTRA VEZ...')