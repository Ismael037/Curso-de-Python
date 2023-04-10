from datetime import date
print('PROGRAMA DE SERVIÇOS DO EB...')
ano = int(input('Digite o seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
print('Você tem {} anos.'.format(idade))
if idade < 18:
    print('Ainda falta {} anos para você se alista.'.format(18-idade))
elif idade == 18:
    print('É hora de se alistar, não perca tempo.')
else:
    print('O seu prazo de alistamento passou a {} anos, se não se alistou vá a uma junta militar para esta em dias com os serviços militares.'.format(idade-18))