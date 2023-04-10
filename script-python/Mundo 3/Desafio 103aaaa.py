def ficha(jog'<DESCONHECIDO>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonate.')


print('-'*20)
n = str(input('Nome do jogador: '))
g = str(input('Números de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
