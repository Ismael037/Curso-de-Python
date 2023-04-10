cont = 0
soma = 0
n = 0
n = int(input('Digite um número [999 se quiser parar]: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número [999 se quiser parar]: '))
print('A quantidade de números que foram digitados foi de: {}'.format(cont))
print('A soma entre eles é de {}'.format(soma))