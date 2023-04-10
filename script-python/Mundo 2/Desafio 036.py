print('ESSE É UM PROGRAMA DE ANALISE DE EMPRÉSTIMO BANCÁRIO..')
casa = float(input('Qual o valor casa que você quer financiar?: '))
sal = float(input('Digite o valor do seu salário mensal: '))
mes = int(input('Quantidade de parcelas: '))
div = casa / mes
parc = div
porce = (sal * 30 / 100)
print('O seu limite de parcela seria de {}'.format(porce))
print('O seu empréstimo seria de R${:.2f} o valor da parcela ficaria de R${:.2f} em {} mêses.'.format(casa, div, mes))
if parc > porce:
    print('Seu empréstimo foi NEGADO, sua renda não é compatível com o valor da casa.')
else:
    print('Empréstimo APROVADO')