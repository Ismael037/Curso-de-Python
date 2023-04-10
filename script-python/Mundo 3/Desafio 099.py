from time import sleep
def maior(*num):
    print('-='*30)
    print('Analisando os valores passados...')
    for c in num:
        print(f'{c}', end=' ')
        sleep(0.5)
    if c == 0:
        print('Foram informados 0 ao todo.')
    else:
        print(f'Foram informados {len(num)} ao todo.')
    print(f'O maior valor informado foi {max(num)}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
