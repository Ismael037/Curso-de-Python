def voto(a):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - nasc
    if idade >= 18 and idade < 70:
        return f'Com {idade} anos: O VOTO É OBRIGATÓRIO'
    elif idade < 18:
        return f'Com {idade} anos: O VOTO É NEGADO'
    else:
        return f'Com {idade} anos: O VOTO É OPCIONAL'


print('=-'*15)
nasc = int(input('Em que ano voce nasceu? '))
print(voto(nasc))
