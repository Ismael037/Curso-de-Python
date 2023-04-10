print('-=-' * 20)
print('Analisador de triangulos')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR triangulo!', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1: #Diferente
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triangulo!')