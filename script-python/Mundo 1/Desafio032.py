from datetime import date
ano = int(input('Que ano quer analisar?' ))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano {} E BISSEXTO'.format(ano))
else:
    print('O ano {} náo é BISSEXTO'.format(ano))