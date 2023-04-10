from random import randint
com = randint (0, 10)
print('-='*20)
print('VAMOS JOGAR PAR OU IMPAR!!')
print('-='*20)
v = 0
esc = ' '
while True:
    jogador = int(input('Diga um valor: '))
    while esc not in "PI":
        esc = str(input('PAR ou IMPAR [P/I]: ')).upper().strip()[0]
    total = jogador + com
    print(f'Você jogou {jogador} e o computador jogou {com}. O Total é {total}', end= '')
    print(' DEU PAR!!' if total % 2 == 0 else ' DEU IMPAR!!')
    print()
    if jogador % 2 == 0:
        if esc in "P":
            print('Você VENCEU!!')
            v += 1
        else:
            print('Voce PERDEU!!')
            break
    elif jogador % 2 == 1:
        if esc in "I":
            print('Você GANHOU!!')
            v += 1
        else:
            print('Você PERDEU!!')
            break
    print('Vamos Continuar!!!')
print(f'GAME OVER Você Venceu {v} Vezes!!')

