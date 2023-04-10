preço = float(input('Qual o valor do produto? R$ '))
por = preço * 5 / 100
des = preço - por
#ou des = preço - (preç * / 100)
print('O Valor do seu produto será de {} R$'.format(des))