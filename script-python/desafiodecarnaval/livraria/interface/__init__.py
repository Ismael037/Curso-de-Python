def leiaInt(msg):
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


def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mErro!: \"{entrada}\" é um preço inválido\033[m')
        else:
            válido = True
            return float(entrada)


def casadeci(a):
    conv = float(a)
    return f'{conv:.2f}'


def linha(tam = 40):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[35mSua Opção: \033[m')
    return opc