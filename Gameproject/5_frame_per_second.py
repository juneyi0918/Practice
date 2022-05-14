import pygame

pygame.init()  # reset

# Size setting

screen_width = 480  # width size
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))


# Game title

pygame.display.set_caption("PANG Game")

# FPS
clock = pygame.time.Clock()


# Load background 
background = pygame.image.load("C:/Users/june's PC/Desktop/CODING/Gameproject/background.png")

# Load Character
character = pygame.image.load("C:/Users/june's PC/Desktop/CODING/Gameproject/character.png")
character_size = character.get_rect().size # get size of chracter image
character_width = character_size[0]  
character_height = character_size[1] 
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height


# Move coordination
to_x = 0
to_y = 0

# Movement speed
character_speed = 0.6 


# Event Loop

running = True # Is game running?

while running:
    dt = clock.tick(500)

    
    print("fps: " + str(clock.get_fps()))
    
    for event in pygame.event.get():  # what event happen?
        if event.type == pygame.QUIT:   # Is is closed?
            running = False
        
        if event.type == pygame.KEYDOWN: # Is keydown happend?
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:  # Is keyup happend?
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # Horizontal min & max
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # Vertical min & max
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height



    screen.blit(background, (0,0))  # apply background
    screen.blit(character, (character_x_pos,character_y_pos))  # apply background


    pygame.display.update() # Reapply background

pygame.quit()
