print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)
total = maior100 = menor = cont =  0
barato = ' '
while True:
    nome = str(input('Nome Do Produto: ')).upper()
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço >= 1000:
        maior100 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome

    esc = ' '
    while esc not in "SN":
        esc = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if  esc == "N":
            break
print('-'*20)
print(f'''O total da compra foi de R$ {total:.2f}
Temos {maior100} produtos custando mais de R$ 1000.00
O produto mais bataro foi {barato} que custa R$ {menor:.2f}''')
