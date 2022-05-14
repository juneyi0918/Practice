import pygame
import os
###########################################################
# Basic reset ( Must DO )
pygame.init()  # reset

# Size setting

screen_width = 640  # width size
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

# Game title

pygame.display.set_caption("Jungle PANG")

# FPS
clock = pygame.time.Clock()
###########################################################

### 1. Custom Game Reset ( Background screen, game image, coordination , spped, font )
current_path = os.path.dirname(__file__)  # current file location
image_path = os.path.join(current_path,"images") # images file location

# Make Background
background = pygame.image.load(os.path.join(image_path,"background.png"))

# Make Stage 
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size [1]  # need character on top of the stage

# Make Character 
character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = (screen_height-character_height-stage_height)

# character move variable
character_to_x = 0

# character move speed 
character_speed = 5 

# Make weapon
weapons = [] # CAN USE multiple weapons at one time 
weapon_speed = 10

weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]


# Make Balloon 

ball_images = [
    pygame.image.load(os.path.join(image_path,"balloon1.png")),
    pygame.image.load(os.path.join(image_path,"balloon2.png")),
    pygame.image.load(os.path.join(image_path,"balloon3.png")),
    pygame.image.load(os.path.join(image_path,"balloon4.png"))]

# different ball speed 
ball_speed_y = [-18,-15,-12,-9]

balls = []

# Initial ball create 
balls.append({
    "pos_x" : 50,   # ball x location
    "pos_y" : 50,   # ball y location
    "img_idx" : 0,
    "to_x" : 3,
    "to_y" : -6,
    "init_spd_y" : ball_speed_y[0]})






# Event Loop

running = True 
while running:
    dt = clock.tick(30)

    # 2. Event (keyboard or mouse)    
    for event in pygame.event.get():  # what event happen?
        if event.type == pygame.QUIT:   # Is is closed?
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:       # Move left
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:    # Move right
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:    # Shoot weapon
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
        
        if event.type == pygame.KEYUP:
            if event.key -- pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

            
    # 3. Game Character position declaration 
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # weapons location 

    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] 

    weapons = [ [w[0],w[1]] for w in weapons if w[1] > 0]


    # ball location 

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]


        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]


        # BALL HORIZONTAL FLIP
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1 
        
        # BALL VERTICAL FLIP
        if ball_pos_y >= screen_height - stage_height - ball_height: 
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["to_y"] += 0.5
        
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]



    # 4. Collision 

    # 5. Draw on screen


    screen.blit(background,(0,0))

    for weapon_x_pos, weapon_y_pos in weapons : 
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pox_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x,ball_pos_y))
    

    screen.blit(stage,(0,screen_height- stage_height))
    
    screen.blit(character,(character_x_pos,character_y_pos))

   


    pygame.display.update() # Reapply background
    
pygame.quit()
