import pygame
from sys import exit
from ctypes import windll
from pygame.locals import * 


windll.shcore.SetProcessDpiAwareness(1)

w, h = [1200, 800]

pygame.init()

# Name and icon
screen = pygame.display.set_mode((w, h), RESIZABLE)
pygame.display.set_caption('The Shilton Diaries')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# Surface for player input
player_sur = pygame.Surface((w, h/3))
player_sur.fill((11, 252, 3))

# Surface for the NPC interactions
NPC_surface = pygame.Surface((w, h*2/3))
NPC_surface.fill((252, 3, 3))

# Player text box
font = pygame.font.Font("fonts/Peepo.ttf", 30)
user_input = ""
text_container = pygame.Rect(w/2,300, 140, 32)
text_container_color = pygame.Color('red')


 # Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_BACKSPACE:
                pygame.key.set_repeat(200, 50) 
                user_input = user_input[:-1]               
            elif event.key == pygame.K_RETURN:
                pass
            else: 
                user_input += event.unicode
                      
    # Draws user input and NPC output boxes
    screen.blit(player_sur,(0, h-h/3))
    screen.blit(NPC_surface, (0,0))

    # Draws user text box 
    pygame.draw.rect(screen,text_container_color,text_container,2,3)
    ui_surface = font.render(user_input,True,(0, 0, 0))
    screen.blit(ui_surface, (text_container.x + 5, text_container.y + 10))
    text_container.w = max(100, ui_surface.get_width() + 10)
    text_container.h = max(50, ui_surface.get_height())
    
    
    
    
    
    
    
            
            
    pygame.display.update()
    clock.tick(60)