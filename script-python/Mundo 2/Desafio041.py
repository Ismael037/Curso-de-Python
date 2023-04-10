from datetime import date
print('-'*62)
print('PROGRAMA DA CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-'*62)
print('Digite sua Data de nasciemnto abaixo para saber sua categoria:')
ano = int(input('DATA: '))
ano_atual = date.today().year
idade = ano_atual - ano
print('SUA IDADE É DE {} anos.'.format(idade))
if idade > 20:
    print('Sua categoria é MASTER.')
elif idade > 19:
    print('Sua categoria é SÊNIO.')
elif idade > 14 :
    print('Sua categoria é JUNIOR.')
elif idade > 9:
    print('Sua categoria é INFANTIL.')
else:
    print('Sua categora é MIRIN.')