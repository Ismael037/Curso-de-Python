n = soma = quant = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    quant += 1
print(f'A soma entre os números é {soma} e a quantidade de número digitados foi de {quant}.')