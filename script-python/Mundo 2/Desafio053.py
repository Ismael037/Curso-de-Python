frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = '' #inverso
for letra in range(len(junto) - 1, -1,-1): #inverso
    inverso += junto[letra] #inverso
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palídromo!')
else:
    print('Não temos um palídromo!')

''' Sem usar o for pode-se usar a segunte formula
inverso = junto[::-1]'''
