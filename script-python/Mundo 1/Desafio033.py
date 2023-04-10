from time import sleep
a = int(input('Digite o primeiro número: '))
b = int(input('O segundo.. : '))
c = int(input('Agora o terceiro: '))
print('PROCESSANDO...')
sleep(2)
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#______________________
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))