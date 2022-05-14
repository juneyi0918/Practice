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
character_size = character.get_rect().size # get size of character image
character_width = character_size[0]  
character_height = character_size[1] 
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height


# Move coordination
to_x = 0
to_y = 0

# Movement speed
character_speed = 0.6 

# Load enemy
enemy = pygame.image.load("C:/Users/june's PC/Desktop/CODING/Gameproject/enemy.png")
enemy_size = enemy.get_rect().size # get size of enemy image
enemy_width = enemy_size[0]  
enemy_height = enemy_size[1] 
enemy_x_pos = (screen_width/2) - (enemy_width/2)
enemy_y_pos = (screen_height/2) - (enemy_height/2)
    


# Event Loop

running = True # Is game running?

while running:
    dt = clock.tick(60)
    
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

    # Horizontal min & max for character position
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # Vertical min & max for character position
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    # rect information update for collision event 

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # collision check

    if character_rect.colliderect(enemy_rect):
        print("GAME OVER: Collision!!")
        running = False




    screen.blit(background, (0,0))  # apply background
    screen.blit(character, (character_x_pos,character_y_pos))  # apply character
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) # apply enemy  


    pygame.display.update() # Reapply background

pygame.quit()
