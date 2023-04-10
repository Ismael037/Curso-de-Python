lista = []
listapar = []
listaimpa = []
while True:
    lista.append(int(input('Digite um número: ')))
    esc = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if esc == "N":
        break
print('=-'*30)
print(f'A lista completa é {lista}')
for n in lista:
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpa.append(n)
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaimpa}')
