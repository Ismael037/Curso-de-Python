somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('--- {} Pesooa ---'.format(p))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: ')).upper().strip()
    somaidade += idade
    if p == 1 and sexo in 'MASCULINO':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'MASCULINO' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'FEMININO' and idade <20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {:.0f} anos.'.format(mediaidade))
print('O Homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('A quantidade de mulheres que tem menos de 20 anos no grupo é de: {};'.format(totmulher20))

