numeros = []
while True:
    esc = ' '
    while esc not in "SN":
        n = int(input('Digite um valor: '))
        if n not in numeros:
            numeros.append(n)
            print('Valor adcionado com sucesso...')
        else:
            print('Valor deplicado! Não vou adicionar..')
        esc = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    if esc == "N":
        break
print('=-'*30)
print(f'Os números digitados foram{sorted(numeros)}')