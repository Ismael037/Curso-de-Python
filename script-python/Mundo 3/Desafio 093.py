dados = {}
gols = []
dados['Nome'] = str(input('Nome do jogador: '))
dados['total']= int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(1,dados['total']+1):
    c = int(input(f'Quantos gols na partida {c}? '))
    gols.append(c)
    dados['Gols'] = gols
print('=-'*20)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}.')
print('=-'*20)
print(f'O jogador {dados["Nome"]} jogou {dados["total"]} partidas.')
for i, v in enumerate(gols):
    print(f'=> Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {sum(gols)} gols.')
