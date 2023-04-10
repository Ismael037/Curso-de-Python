#frase = (input('Digite um número para saber detalhes: '))
#posi1 = frase.split()
#uni = (posi1[0][0])
#print('unidade: {} '.format(uni))
#dez = (posi1[0][1])
#print('Dezena: {}'.format(dez))
#cen = (posi1[0][2])
#print('Centena: {}'.format(cen))
#mil = posi1[0][3]
#print('Milhar: {}'.format(mil))
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando número...')
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('centena: {}'.format(c))
print('Milhar: {}'.format(m))