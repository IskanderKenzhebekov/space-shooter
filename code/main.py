import pygame
from os.path import join # That will allow me to not bother about the right path to the files I need to use.
from random import randint

# general setup 
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720 # The values we put for the display resolution
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # code to open a dispaly
pygame.display.set_caption("Space Shooter") 
running = True
clock = pygame.time.Clock() # The code can control the frame rate 

  
# plainsurface (Just to see how to create surface and place it in display)
surf = pygame.Surface((100,200)) # Need to be attached to dispalay surface
surf.fill ("yellow")

# importing an image 
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha() # "conver.alpha" - allows to improve performances of surfaces dramatically (more frame rates)
player_rect = player_surf.get_frect(midbottom = (WINDOW_WIDTH /2 , WINDOW_HEIGHT - 200))
player_direction = pygame.math.Vector2() # As the default should be 0 and 0
player_speed = 300

meteor_surf = pygame.image.load (join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load (join('images', 'laser.png'))
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20 ))

star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha() 
star_positions = [(randint(0, 1280), randint(0,720)) for i in range (20)]

while running: 
    dt = clock.tick() /1000
    # Event loop 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        #if event.type == pygame.KEYDOWN and event.key == pygame.K_1: /// I did this as a comment, since I realized that there better way to do player movement than in the loop (outside of the loop obviously)
            #print(1)                                                 /// That's because if I am going to hold any button I will only get one output
        #if event.type == pygame.MOUSEMOTION:                         /// However, If I do it outside of the loop I will get output as long as I hold the buttons
            #player_rect.center = event.pos
            

    # Input
    #pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT]) # This is the proper way to set the to control the player motion
    player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    player_direction = player_direction.normalize() if player_direction else player_direction # This code is to normalize the speed of the player when he moves diagonally (it used to be faster)
    player_rect.center += player_direction * player_speed * dt
    
    
            
    # Draw the game 
    display_surface.fill('darkgrey') # to fill the space in blue
    for pos in star_positions:
        display_surface.blit(star_surf, pos)
    

    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)
    display_surface.blit(player_surf, player_rect.topleft) # code to put one surface (The player.png in this case) on another surface (Origin point is on the top left)


    pygame.display.update()
    
    

    
pygame.quit() # opposite to "pygame.init()". Better to put at the end (may cause bugs otherwise)
      
    