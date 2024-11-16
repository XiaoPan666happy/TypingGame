"""主程序文件"""

import pygame
from config import *

pygame.init()
pygame.font.init()

def start(screen:pygame.surface.Surface, 
          font_big:pygame.font.Font,
          font_small:pygame.font.Font) -> bool:
    """封面"""
    while not(pygame.key.get_pressed()[pygame.K_RETURN]):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        # 没啥逻辑 把背景渲染一下
        text1 = font_big.render("打字游戏", True, (63, 72, 204))
        text2 = font_small.render("Please pressed enter and play the game", True, (63, 72, 204))
        screen.fill((255, 255, 255))
        screen.blit(text1, (200, 200))
        screen.blit(text2, (200, 350))

        pygame.display.flip()

    return True

def play_game(screen:pygame.surface.Surface, 
              font:pygame.font.Font,
              font_small:pygame.font.Font) -> None:
    """主函数"""
    pass

def main() -> None:
    """控制函数"""
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("打字游戏")
    font_big = pygame.font.Font(os.path.join(PATH, "font", "STKAITI.TTF"), 100)
    font_small = pygame.font.Font(os.path.join(PATH, "font", "STKAITI.TTF"), 25)
    if start(screen, font_big, font_small):
        play_game(screen, font_big, font_small)

if __name__ == "__main__":
    main()

pygame.font.quit()
pygame.quit()
