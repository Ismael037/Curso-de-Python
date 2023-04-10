from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['CTPS'] = int(input('Carteira de trabalho: (0 não tem)  '))
dados['Idade'] = datetime.now().year - nasc
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = dados['Idade'] + (dados['Contratação'] +35 - datetime.now().year)
print('=-' *30)
for k, v in dados.items():
    print(f' - {k} tem valor {v}')