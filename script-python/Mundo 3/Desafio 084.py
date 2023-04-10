pessoas = []
dados = []
peso = []
maior = menor = 0
cont = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    esc = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    pessoas.append(dados[:])
    dados.clear()
    cont += 1
    if esc == "N":
        break
print(f'Ao todo, você cadastrou {cont} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg. peso de ',end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]',end='')
print()
print(f'O menor peso foi de {menor:.1f}Kg. peso de ',end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]',end='')