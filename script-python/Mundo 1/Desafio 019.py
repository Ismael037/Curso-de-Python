from random import choice
a1 = input('Pimeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
escolha = choice(lista)
print('O aluno escolhido foi {}'.format(escolha))