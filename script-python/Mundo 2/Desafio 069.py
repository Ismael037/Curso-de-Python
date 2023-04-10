somaidade = somafem = somamascu = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    if idade >= 18:
        somaidade += 1
    while sexo not in "MF":
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if sexo in "F":
            if idade < 20:
                somafem += 1
        elif sexo in "M":
            somamascu += 1
    cont = ' '
    while cont not in "SN":
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont in "N":
        break
print(f'{somaidade} Pessoas em idade maior que 18 anos foram cadastradas.')
print(f'{somamascu} Homens foram cadastrados.')
print(f'{somafem} Mulheres menos de 20 anos foram cadastradas.')
