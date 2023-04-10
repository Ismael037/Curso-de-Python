'''from math import factorial
num = int(input('Digite um número: '))
f = factorial(num)
print('O fatorial de {} é {}'.format(num, f)'''

num = int(input('Digite um número: '))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))