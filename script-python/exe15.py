dia = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos Km foram rodados? Km '))
valor = (dia * 60) + (km * 0.15)

print('O valor a pagar é de R${:.2f}'.format(valor))