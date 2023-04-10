nome = str(input('Digite seu nome para saber todas as informações sobre ele: ')).strip()
print('Analisando seu nome...')
print('Seu nome em letras maiusculas é: {} '.format(nome.upper()))
print('Seu nome com letras minusculas é: {} '.format(nome.lower()))
quant = (nome.strip()) #nome sem espaço
cont = len(quant) - nome.count(' ') #quantidade de letras
print('A quantidade de letras que tem no seu nome é {} '.format(cont))
qua = (nome.split()) #dividindo pra tirar so o primeiro nome
posi = (qua[0])#posição do primeiro nome
qtr = len(posi)#contagem de letras do primeiro nome
print('A quantidade de letras do seu primeiro nome é de {} letras'.format(qtr))


