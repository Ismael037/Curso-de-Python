dados = []
pessoas = {}
mulheres = {}
cont = 0
somaidade = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper()
    while pessoas['sexo'] not in "M/F":
        pessoas['sexo'] = str(input('ERRO! Por favor, digite apenas [M/F] ')).upper()
    pessoas['idade'] = int(input('Idade: '))
    somaidade += pessoas['idade']
    dados.append(pessoas.copy())
    opc = str(input('Quer continuar? [S/N] ')).upper()
    while opc not in "SN":
        opc = str(input('ERRO! Responda apenas [S/N] ')).upper()
    cont += 1
    if opc in "N":
        break
media = somaidade / cont
print('=-'*30)
print(f'A) Ao todo temos {cont} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram ',end='')
for c in dados:
    if c["sexo"] in "F":
        print(f'{c["nome"]} ', end='')
print(f'\nD) Lista das pessoas que estão acima da média: ')
for c in dados:
    if c["idade"] >= media:
        print(f'nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]}')

