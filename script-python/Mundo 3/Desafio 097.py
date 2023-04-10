def traços(a):
    for c in range(1, len(f) + 5):
        print('-', end='')
def linhas(a):
    traços(a)
    print(f'\n  {f}')
    traços(a)


f = str(input(' Digite a frase para formatar: '))
linhas(f)


