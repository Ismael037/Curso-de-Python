print('-' *12)
print('CALCULADORA')
print('-' *12)
n = int(input('Digite um número: '))
for c in range(1, 11):
    mult = c * n
    print('{:2} X {} = {}'.format(c, n,mult))
