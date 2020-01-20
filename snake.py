import pygame

run = True
pygame.display.init()
screen_width = 500
screen_height = 500
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.toggle_fullscreen()

while run == True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False




