import pygame

pygame.init()  # reset

# Size setting

screen_width = 480  # width size
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))


# Game title

pygame.display.set_caption("PANG Game")


running = True # Is game running?

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
