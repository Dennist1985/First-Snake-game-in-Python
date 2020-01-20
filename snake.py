import pygame

run = True
pygame.init()
screen_width = 1000
screen_height = 1000
snakeColor = (255,0,0)

# The window is made.
screen = pygame.display.set_mode([screen_width, screen_height])

# The snake is drawn as a rectangle in center of window.
snake = pygame.draw.rect(screen, snakeColor, (495, 495, 10, 10))

# This is the a loop where the display keeps updating.
# And to keep the window alive unless you close it yourself.
while run == True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False
    pygame.display.update()





