import random
import pygame
###########################################################
# Basic reset ( Must DO )
pygame.init()  # reset

# Size setting

screen_width = 480  # width size
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# font
game_font = pygame.font.Font(None, 40)

# Game title

pygame.display.set_caption("QUIZ")

# FPS
clock = pygame.time.Clock()

###########################################################

### 1. Custom Game Reset ( Background screen, game image, coordination , spped, font )

# Background
background = pygame.image.load("C:/Users/june's PC/Desktop/CODING/Gameproject/pygame_project/images/wood dot background.png")

# Character
character = pygame.image.load ("C:\\Users\\june's PC\\Desktop\\CODING\\Gameproject\\cute chick.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = (screen_height - character_height)

to_x = 0

character_speed = 10


# Load enemy
enemy = pygame.image.load("C:/Users/june's PC/Desktop/CODING/Gameproject/snake.png")
enemy_size = enemy.get_rect().size # get size of enemy image
enemy_width = enemy_size[0]  
enemy_height = enemy_size[1] 
enemy_x_pos = random.randint(0,screen_width-enemy_width)
enemy_y_pos = 0
enemy_speed = 10

enemy1 = pygame.image.load("C:/Users/june's PC/Desktop/CODING/Gameproject/snake.png")
enemy1_size = enemy1.get_rect().size # get size of enemy image
enemy1_width = enemy1_size[0]  
enemy1_height = enemy1_size[1] 
enemy1_x_pos = random.randint(0,screen_width-enemy1_width)
enemy1_y_pos = 0
enemy1_speed = 20

# Score
score= 0
# Event Loop

pygame.time.delay(2000)

running = True 
while running:
    dt = clock.tick(50)

    # 2. Event (keyboard or mouse)    
    for event in pygame.event.get():  # what event happen?
        if event.type == pygame.QUIT:   # Is is closed?
            running = False

        if event.type == pygame.KEYDOWN: # Is keydown happend?
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
         

        if event.type == pygame.KEYUP:  # Is keyup happend?
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
         

    # 3. Game Character position declaration 

    character_x_pos += to_x 


     # Horizontal min & max for character position
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # enemy position
    enemy_y_pos += enemy_speed
    enemy1_y_pos += enemy1_speed
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0,screen_width-enemy_width)
        score += 10

    if enemy1_y_pos > screen_height:
        enemy1_y_pos = 0
        enemy1_x_pos = random.randint(0,screen_width-enemy1_width)
        score += 10
    

    




    score_print = game_font.render(str(int(score)), True,(255,255,255) )



    # 4. Collision 
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
   

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    enemy1_rect = enemy1.get_rect()
    enemy1_rect.left = enemy1_x_pos
    enemy1_rect.top = enemy1_y_pos

    if character_rect.colliderect(enemy_rect):
        print("Collision!")
        running = False

    if character_rect.colliderect(enemy1_rect):
        print("Collision!")
        running = False

    # 5. Draw on screen

    screen.blit(background, (0,0))  # apply background
    screen.blit(character, (character_x_pos,character_y_pos))  # apply character
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    screen.blit(enemy1,(enemy1_x_pos,enemy1_y_pos))  
    screen.blit(score_print,(10,10))
    pygame.display.update() # Reapply background

print(f"your score is : {score}")    

pygame.time.delay(2000)
pygame.quit()
