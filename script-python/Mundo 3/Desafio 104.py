def leiInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO')
        if ok:
            break
    return valor

n = leiInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
