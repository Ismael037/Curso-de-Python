from random import randint
from time import sleep
com = randint(0,10)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10. tente adivinhar...')
print('-=-'*20)
cont = 0
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
while com != jogador:
    if jogador < com:
        print('Mais...')
    else:
        print('Menos..')
    jogador = int(input('Você NÃO acertou, tente novamente: '))
    cont += 1
    sleep(1.8)
print('Você acertou, o COMPUTADOR pesou no número {}!! '.format(com))
print('O número de palpites necessários para você acertar foi {}!'.format(cont))
