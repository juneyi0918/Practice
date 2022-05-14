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

# Load Character
character = pygame.image.load("C:/Users/june's PC/Desktop/CODING/Gameproject/character.png")
character_size = character.get_rect().size # get size of chracter image
character_width = character_size[0]  
character_height = character_size[1] 
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height




running = True # Is game running?

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))  # apply background
    screen.blit(character, (character_x_pos,character_y_pos))  # apply background


    pygame.display.update() # Reapply background

pygame.quit()
