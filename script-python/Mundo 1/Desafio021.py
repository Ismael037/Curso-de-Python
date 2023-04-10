import pygame
pygame.init()
som = pygame.mixer.Sound("ex0.mp3")
som.play()
run = True
while run:
 for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  run = False