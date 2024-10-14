import pygame
from os.path import join # That will allow me to not bother about the right path to the files I need to use.
from random import randint


class Player (pygame.sprite.Sprite): 
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH /2 , WINDOW_HEIGHT / 2))
        self.direction = pygame.Vector2()
        self.speed = 300
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT]) # This is the proper way to set the to control the player motion
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction # This code is to normalize the speed of the player when he moves diagonally (it used to be faster)
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys [pygame.K_SPACE]: 
            print ("fire lazer")
    
class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0, 1280), randint(0,720)))



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

all_sprites = pygame.sprite.Group()
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha() 
for i in range (20): 
    Star(all_sprites, star_surf)
player = Player(all_sprites)

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
      
    # Update
    all_sprites.update(dt)
            
    # Draw the game 
    display_surface.fill('darkgrey') # to fill the space in blue
    all_sprites.draw(display_surface)
    
    
    pygame.display.update()
    


    
pygame.quit() # opposite to "pygame.init()". Better to put at the end (may cause bugs otherwise)
      
    