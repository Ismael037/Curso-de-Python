dis = float(input('Qual a distancia da sua viagem? Km/h '))
if dis <= 200:
    cal = 0.50 * dis
    print('O valor da sua viagem será de R$ {:.2f}.'.format(cal))
else:
    cal2 = 0.45 * dis
    print('O valor da viagem será de R$ {:.2f}'.format(cal2))