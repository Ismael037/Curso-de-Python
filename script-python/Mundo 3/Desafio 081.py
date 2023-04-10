listagem = []
while True:
    listagem.append(int(input('Difite um valor: ')))
    esc = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if esc == "N":
        break
print('=-'*30)
print(f'Voce digitou {len(listagem)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(listagem,reverse=True)}')
if 5 in listagem:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')