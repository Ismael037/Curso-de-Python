valores = [[], []]
v = 0
for v in range(0, 7):
    v = int(input(f'Digite o {v+1}. valor:  '))
    if v % 2 == 0:
        valores[0].append(v)
    else:
        valores[1].append(v)
print(f'Os valores pares digitados foram: {sorted(valores[0])}')
print(f'Os valores ímpares digitados foram: {sorted(valores[1])}')

