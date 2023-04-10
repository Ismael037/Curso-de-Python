from random import shuffle
a1 = input('Digite o nome: ')
a2 = input('Digite o nome: ')
a3 = input('Digite o nome: ')
a4 = input('Digite o nome: ')

lista = [a1, a2, a3, a4]
ordem = shuffle(lista)

print('A ordem será')
print(lista)