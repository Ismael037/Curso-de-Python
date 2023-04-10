print('PROGRAMA DE PREÇO E DESCONTOS...')
preco = float(input('Digite o valor do produto: R$ '))
print('Qual a forma de pagamento? \n(1) Dinheiro/Cheque\n(2) Cartão')
avista = int(input('Digite o número da opção desejada: '))
if avista == 2:
    vezes = int(input('Quantas vezes você irá dividir? '))
    if vezes > 2:
        juros = preco + (preco * 20 / 100)
        print('O valor do produto ficará R$ {:.2f} Dividido em {} vezes.'.format(juros, vezes))
    elif vezes > 1:
        print('O valor do produto fica R$ {:.2f} Dividido em {} vezes.'.format(preco, vezes))
    else:
        desc = preco - preco * 5 / 100 #desconto de 5%
        print('O valor do produto fica R$ {:.2f} á vista no cartão. '.format(desc))
elif avista == 0:
    print('Opção INVALIDA')
elif avista ==1:
    desc = preco - (preco * 10 / 100) #desconto de 10%
    print('O valor do produto á vista fica R${:.2f}.'.format(desc))




