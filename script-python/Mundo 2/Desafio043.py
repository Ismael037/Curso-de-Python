print('ATRAVEZ DESSE PROGRAMA VOCÊ IRÁ SEU IMC..')
peso = float(input('Digite o seu peso: '))
altura = float(input('Agora digite sua altura: '))
imc = peso / (altura * altura) #ou |altura ** 2|
print('O seu IMC é {:.2f}.'.format(imc))
if imc > 40:
    print('Você está com OBESIDADE MÓRBIDA, precisa se cuidar urgentemente.')
elif imc > 30:
    print('O status de peso é : OBESIDADE, cuidado!!, Cuide-se mais!.')
elif imc > 25:
    print('Você está em SOBREPESO, isso quer dizer que está um pouco acima do peso, cuide-se!.')
elif imc > 18.5:
    print('Muito bom o seu peso é cosiderado IDEAL, Parabens!!')
else:
    print('Você está ABAIXO DO PESO, procure se tratar mais!!.')