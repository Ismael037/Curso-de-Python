sal = float(input('Qual o seu salário: R$ '))
if sal > 1250:
    aum1 = sal + (sal * 10 / 100)
    print('O seu novo salário será de R$ {:.2f}'.format(aum1))
else:
    aum2 = sal + (sal * 15 / 100)
    print('o seu novo salário será de R$ {:.2f}'.format(aum2))