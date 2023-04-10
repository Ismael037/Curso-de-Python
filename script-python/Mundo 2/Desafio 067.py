while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    print('-'*30)
    if n < 0:
        break
    for quant in range(1, 11):
        mult = n * quant
        print(f'{n} x {quant} = {mult} ')
    print('-'*30)
print('Programa TABUADA ENCERRADO...')