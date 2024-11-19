"""主程序文件"""

import time
import random

import pygame

from config import *
import letter
import letter_group

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
        screen.blit(text1, (195, 175))
        screen.blit(text2, (215, 325))
        pygame.display.flip()

    return True

def play_game(screen:pygame.surface.Surface, 
              font_big:pygame.font.Font,
              font_small:pygame.font.Font) -> None:
    """主函数"""
    
    score = 0        # 得分
    miss = 0         # 遗漏
    combo = 0        # 连击
    play_time = 0.0  # 时间
    
    start_time = time.time()
    clock = pygame.time.Clock()
    i = 0
    my_letter_group = letter_group.LetterGroup()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if my_letter_group.key_doun_(i):
            my_letter_group.out(i)
            combo += 1
            score += 1
        elif my_letter_group.need_del_():
            my_letter_group.out()
            score += combo * (combo // 2)
            combo = 0
            miss += 1
        
        if i % 100 == 0:
            my_letter_group.add(letter.Letter(chr(random.randint(65, 90)), font_big, random.randint(10, 690)))

        play_time = round((time.time() - start_time), 1)
        fps = int(clock.get_fps())

        text_fps = font_small.render(f"帧率    {fps}", True, (0, 0, 0))
        text_time = font_small.render(f"时间    {play_time}", True, (0, 0, 0))
        text_score = font_small.render(f"得分    {score}", True, (0, 0, 0))
        text_miss = font_small.render(f"遗漏    {miss}", True, (0, 0, 0))
        if combo >= 2:
            text_combo = font_small.render(f"连击 {combo}", True, (0, 0, 0))
        else:
            text_combo = None
        
        for my_letter in my_letter_group:
            my_letter.update()

        # 渲染
        screen.fill((255, 255, 255))
        for my_letter in my_letter_group:
            my_letter.draw(screen)
        screen.blit(text_fps, (10, 10))
        screen.blit(text_time, (10, 40))
        screen.blit(text_score, (10, 70))
        screen.blit(text_miss, (10, 100))
        if not(text_combo is None):
            screen.blit(text_combo, (350, 390))
        pygame.display.flip()
        
        # 控制帧率
        clock.tick(FPS)

        i += 1

def init() -> tuple:
    """初始化"""
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("打字游戏")
    font_big = pygame.font.Font(os.path.join(PATH, "font", "STKAITI.TTF"), 100)
    font_small = pygame.font.Font(os.path.join(PATH, "font", "STKAITI.TTF"), 25)
    return (screen, font_big, font_small)

def main() -> None:
    """控制函数"""
    screen, font_big, font_small = init()
    if start(screen, font_big, font_small):
        play_game(screen, font_big, font_small)

if __name__ == "__main__":
    main()

pygame.font.quit()
pygame.quit()
