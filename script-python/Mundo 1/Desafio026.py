nome = str(input('Digite seu nome para saber mais informações: ')).upper().strip()
print('A quantidade de letras "a" no seu nome é de: {}'.format(nome.count('A')))
print('A letra "a" aparece a primeira vez na posiçã0: {} '.format(nome.find('A')+1))
print('A letra "a" no último nome aparece na posição: {}'.format(nome.rfind('A')+1))