import pygame
from os.path import join # That will allow me to not bother about the right path to the files I need to use.
from random import randint

# general setup 
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720 # The values we put for the display resolution
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # code to open a dispaly
pygame.display.set_caption("Space Shooter") 

running = True

  
# plainsurface (Just to see how to create surface and place it in display)
surf = pygame.Surface((100,200)) # Need to be attached to dispalay surface
surf.fill ("yellow")

# importing an image 
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha() # "conver.alpha" - allows to improve performances of surfaces dramatically (more frame rates)
player_rect = player_surf.get_frect(midbottom = (WINDOW_WIDTH /2 , WINDOW_HEIGHT - 200))
player_direction = 1

meteor_surf = pygame.image.load (join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load (join('images', 'laser.png'))
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20 ))

star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha() 
star_positions = [(randint(0, 1280), randint(0,720)) for i in range (20)]

while running: 
    # event loop 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
            
    # draw the game 
    display_surface.fill('darkgrey') # to fill the space in blue
    for pos in star_positions:
        display_surface.blit(star_surf, pos)
    

    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)
    display_surface.blit(player_surf, player_rect) # code to put one surface (The player.png in this case) on another surface (Origin point is on the top left)

      # Player movement
    player_rect.x += player_direction * 0.5
    if player_rect.left <= 0 or player_rect.right >= WINDOW_WIDTH: #This code makes the spaceship stop at the point when it will hit the end of the display
        player_direction = -player_direction

           
  
    pygame.display.update()
    
    

    
pygame.quit() # opposite to "pygame.init()". Better to put at the end (may cause bugs otherwise)
      
    