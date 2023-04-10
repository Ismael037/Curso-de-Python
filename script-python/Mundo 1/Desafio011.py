larg = float(input('Largura da parede'))
alr = float(input('Altura da parede'))
área = larg * alr
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2.'.format(larg, alr, área))
tinta = área / 2
print('Para pintar essa parede, voce precisa de {}l de tinta.'.format(tinta))