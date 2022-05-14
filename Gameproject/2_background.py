import pygame

pygame.init()  # reset

# Size setting

screen_width = 480  # width size
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))


# Game title

pygame.display.set_caption("PANG Game")

# Load background 
background = pygame.image.load("C:/Users/june's PC/Desktop/CODING/Gameproject/background.png")

running = True # Is game running?

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))  # apply background

    pygame.display.update() # Reapply background

pygame.quit()
