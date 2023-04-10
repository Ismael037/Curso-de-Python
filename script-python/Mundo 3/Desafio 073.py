tabela = ("Palmeiras", "Internacional", "Fluminense", "Corintians",
          "Flamengo", "Atletico PR", "Atletico Mg", "Fortaleza",
          "São Paulo", "Botafogo", "América-MG", "Santos", "Goiás",
          "Red Bull Bragantino", "Coritiba", "Cuiabá", "Ceará", "Atlético-GO",
          "Avaí", "Juventude")
print(f'Lista dos times do Brasilerão {tabela}')
print(f'Os 5 primeiros Colocados São{tabela[0:5]}')
print(print(f'Os 4 últimos colocados são {tabela[-4:]}'))
print(sorted(tabela))
print(f'O Flamento esta na {tabela.index("Flamengo")+1} posição.')
