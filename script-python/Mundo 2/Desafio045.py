from random import randint
from time import sleep
import pygame
print('\033[1;32;40mPEDRA, PAPEL TESOURA!!..... VAMOS???\033[m')
jogador = int(input('\033[4;3mFaca sua escolha:\033[m \n1) PEDRA \n2) PAPEL \n3) TESOURA \nR: ' ))
sort = randint(1, 3)
if jogador == 1:
    print('\033[4;31;40mVoce escolheu Pedra\033[m')
elif jogador == 2:
    print('\033[4;31;40mVoce escolheu PAPEL\033[m')
elif jogador == 3:
    print('\033[4;31;40mVoce escolheu TESOURA\033[m')
print('\033[1;36mPEDRA..')
sleep(1)
print('PAPEL..')
sleep(1)
print('TESOURAAA!!\033[m')
    #___________________________________-
if jogador == sort:
    print('\033[0;33;40mIII EMPATOU!! Vamos novamente!!\033[m')
if jogador == 3 and sort == 1:
    print('\033[1;30;42mGANHEI!!!!! Deu PEDRA\033[m')
    pygame.init()
    som = pygame.mixer.Sound("riso01.mp3")
    som.play()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
if jogador == 1 and sort == 2:
    print('\033[1;30;42mGANHEI!!!!! Deu PAPEL\033[m')
    pygame.init()
    som = pygame.mixer.Sound("riso01.mp3")
    som.play()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
if jogador == 2 and sort == 3:
    print('\033[1;30;42mGANHEI!!!!! Deu TESOURA\033[m')
    pygame.init()
    som = pygame.mixer.Sound("riso01.mp3")
    som.play()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
   # _______________
if sort == 3 and jogador == 1:
    print('\033[1;30;42mVOCE GANHOU!! Deu PEDRA\033[m')
    pygame.init()
    som = pygame.mixer.Sound("ex0.mp3")
    som.play()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
if sort == 1 and jogador ==2:
    print('\033[1;30;42mVOCE GANHOU!! Deu PAPEL\033[m')
    pygame.init()
    som = pygame.mixer.Sound("ex0.mp3")
    som.play()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
if sort == 2 and jogador == 3:
    print('\033[1;30;42mVOCE GANHOU!! Deu TESOURA\033[m')
    pygame.init()
    som = pygame.mixer.Sound("ex0.mp3")
    som.play()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
if sort == 1:
    print('\033[4;37;40mEu escolhi Pedra\033[m')
elif sort == 2:
    print('\033[4;37;40mEu escolhi PAPEL\033[m')
elif sort == 3:
    print('\033[4;37;40mEu escolhi TESOURA\033[m')
