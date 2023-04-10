def ficha():
    if nome == "":
        print(f'O jogador <DESCONHECIDO> fez {gols} gol(s) no campeonate.')
    elif gols == '':
        print(f'O jogador {nome} fez 0 gol(s) no campeonate.')
    elif gols == '' and nome == "":
        print(f'O jogador <DESCONHECIDO> fez 0 gol(s) no campeonate.')
    else:
        print(f'O jogador {nome} fez {gols} gol(s) no campeonate.')

print('-'*20)
nome = str(input('Nome do jogador: '))
gols = (input('Números de Gols: '))
ficha()
