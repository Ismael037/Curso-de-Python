sexo = str(input('Qual é seu sexo (M/F): ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dados invalidos, por favor digite seu sexo: ')).strip().upper()[0]
print('A opção foi {}'.format(sexo))
