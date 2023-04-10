from  random import  randint
n1 = (randint(1, 10), randint(1,10), randint(1, 10),
      randint(1,10), randint(1, 10))
print(f'Os valores sortados foram: ', end='')
for n in n1:
    print(f'{n} ', end= '')
print(f'\nO maior valor sortado foi: {max(n1)} ')
print(f'O menor valor sortado foi: {min(n1)} ')
