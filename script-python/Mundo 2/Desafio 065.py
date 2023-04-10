resp = 'Ss'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    quant += 1
    soma += núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
media = soma / quant
print(f'Voce digitou {quant} números e a média foi {media:.1f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
