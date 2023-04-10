velocidade = float(input('Qual a Velocidade do carro? km/h '))
if velocidade >80:
    mul = (velocidade-80) * 7
    print('Voce foi multado! Terá que pagar R$ {} de multa por ultrapassar o limite de velocidade!!'.format(mul))
