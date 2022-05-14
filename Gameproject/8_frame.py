import pygame
###########################################################
# Basic reset ( Must DO )
pygame.init()  # reset

# Size setting

screen_width = 480  # width size
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# Game title

pygame.display.set_caption("PANG Game")

# FPS
clock = pygame.time.Clock()

###########################################################

### 1. Custom Game Reset ( Background screen, game image, coordination , spped, font )

# Event Loop

running = True 
while running:
    dt = clock.tick(60)

    # 2. Event (keyboard or mouse)    
    for event in pygame.event.get():  # what event happen?
        if event.type == pygame.QUIT:   # Is is closed?
            running = False
    # 3. Game Character position declaration 
    
    # 4. Collision 

    # 5. Draw on screen

   


    pygame.display.update() # Reapply background
    
pygame.quit()
