import pygame
from main import *

def drawtextinput():
    pygame.draw.rect(screen,text_container_color,text_container,2,3)
    ui_surface = font.render(user_input,True,(0, 0, 0))
    screen.blit(ui_surface, (text_container.x + 5, text_container.y + 10))
    text_container.w = max(100, ui_surface.get_width() + 10)
    text_container.h = max(50, ui_surface.get_height())