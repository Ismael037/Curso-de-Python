def leiInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\003[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('\033[31mERRO!! Por favor, digite um número Real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO!! Usuário preferiu não digitar o número.\033[m')
            return 0
        else:
            return n


n = leiInt('Digite um número Inteiro: ')
n2 = leiaFloat('Digite um número Real: ')
print(f'Você acabou de digitar o número {n} e o real foi {n2}')
