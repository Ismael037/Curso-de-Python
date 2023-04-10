from datetime import date
s = 0
cont = 0
for c in range(1, 8):
    p1 = int(input('{} Pessoa, Que ano você nasceu? '.format(c)))
    anoatu = date.today().year
    idade = anoatu - p1
    if idade < 21:
        s += 1
    if idade >= 21:
        cont += 1
print('{} pessoas são de maior idade'.format(cont))
print('{} pessoas são de menor idade'.format(s))



