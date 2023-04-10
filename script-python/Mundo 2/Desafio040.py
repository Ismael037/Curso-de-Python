print('APROVADO OU REPROVADO?')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
print('Sua média foi {:.1f}.'.format(media))
if media > 6.9:
    print('Voce foi APROVADO!!')
elif media > 5.0 and media < 7.0:
    print('Você esta de RECUPERAÇÃO, sua nota não foi o suficiente para ser aprovado.')
else:
    print('Você foi REPROVADO, estude mais!')