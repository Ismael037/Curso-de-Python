from time import sleep
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
opcao = 0
maior = 0
while opcao != 5:
    print('''    [1] somar 
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('Qual a opcão?: '))
    if opcao == 1:
        soma = valor1 + valor2
        print('A soma entre {} + {} é {};'.format(valor1, valor2, soma))
    elif opcao == 2:
        mult = valor1 * valor2
        print('A multiplicação entre {} x {} é {};'.format(valor1,valor2,mult))
    elif opcao == 3:
        if valor1 > valor2:
            print('O maior número é {}'.format(valor1))
        else:
            print('O maior número é {}'.format(valor2))
    elif opcao == 4:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    else:
        print('Opção invaálida!!!')
print('SAINDO...')
sleep(1.5)
print('Fim do programa...')