from random import randint
print('-='*20)
print('VAMOSJOGAR PAR OU ÍMPAR;')
print('-='*20)
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    com = randint(1, 10)
    soma = jogador + com
    print(com)
    esc = ' '
    while esc not in "PI":
        esc = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {jogador} e computador {com}. Total de {soma}!!', end='')
    print(' DEU PAR!!' if soma % 2 == 0 else ' DEU IMPAR!!')
    if esc == "P":
        if soma % 2 == 0:
            print('Você Venceu!!')
            v += 1
        else:
            print('Você Pardeu!!')
            break
    elif esc == "I":
        if soma % 2 == 1:
             print('Você Venceu!!')
             v += 1
        else:
            print('Você Perdeu!!')
            break
    print('Vamos jogar novamente!!')
print(f'GAME OVER! Você venceu {v} vezes.')