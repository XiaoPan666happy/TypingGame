"""字母类"""

import pygame

from config import *


class Letter:
    """字母类"""

    def __init__(self, letter:str, font:pygame.font.Font, x:int) -> None:
        self.letter = letter
        self.font = font
        self.x = x
        self.y = -100

    def update(self):
        self.y += SPEED

    def draw(self, screen:pygame.surface.Surface):
        text = self.font.render(self.letter, True, (63, 72, 204))
        screen.blit(text, (self.x, self.y))
    
    def need_del_(self) -> bool:
        if self.y > 600:
            return True
        return False
    
    def key_doun_(self) -> bool:
        keys = pygame.key.get_pressed()
        if keys[ord(self.letter)] and self.y > 0:
            return True
        if keys[ord(self.letter.lower())] and self.y > 0:
            return True
        return False