"""主程序文件"""

import pygame
from config import *

pygame.init()

def start(screen:pygame.surface.Surface) -> bool:
    """封面"""
    while not(pygame.key.get_pressed()[pygame.K_RETURN]):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        # 没啥逻辑 把背景渲染一下
        screen.fill((200, 200, 255))
        pygame.display.flip()

    return True

def play_game(screen:pygame.surface.Surface) -> None:
    """主函数"""
    pass

def main() -> None:
    """控制函数"""
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("打字游戏")
    if start(screen):
        play_game(screen)

if __name__ == "__main__":
    main()

pygame.quit()