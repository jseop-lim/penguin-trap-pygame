import pygame, sys
import random
from pygame.locals import *
from block_control import *
from render import *


# 시작 화면
def start_screen():
    timer = 0
    while True:
        DISPLAYSURF.blit(IMGBOX['start_text'], (0, 0))
        timer = blink_text(timer, 'start')
        is_clicked = False
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()
            elif event.type == MOUSEBUTTONUP:
                is_clicked = True
            elif event.type == KEYDOWN:
                return 0

        if is_setting_hover(mouse_pos):
            if is_clicked:
                game_mode = setting()
                if game_mode != 0:
                    return game_mode
            else:
                DISPLAYSURF.blit(IMGBOX['setting_btn'][0], (0, 0))
        elif is_clicked:
            return 0

        pygame.display.update()
        FPSCLOCK.tick(FPS)


# 설정 화면
def setting():
    img_num = 0
    while True:
        DISPLAYSURF.blit(IMGBOX['setting'][img_num], (0, 0))

        is_clicked = False
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()
            elif event.type == MOUSEBUTTONUP:
                is_clicked = True

        if is_clicked and is_setting_hover(mouse_pos):
            return 0

        img_num = get_setting_num_at_pos(mouse_pos)
        if is_clicked and img_num!=0:
            return img_num

        pygame.display.update()
        FPSCLOCK.tick(FPS)


# 펭귄 위치 반환
def get_center(game_mode):
    if game_mode != 2:
        return CENTER

    timer = 0
    while True:
        DISPLAYSURF.blit(IMGBOX['board_text'], (0, 0))
        timer = blink_text(timer, 'board')
        is_clicked = False
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()
            elif event.type == MOUSEBUTTONUP:
                is_clicked = True

        block_num = get_block_num_at_pos(mouse_pos)

        if block_num != WALL:
            if is_clicked:
                return block_num
            else:
                draw_penguin(block_num)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


# 메인 루프
def run_game(game_mode):
    game_over = False
    center = get_center(game_mode)
    turn = random.choice([PLAYER1, PLAYER2])

    while not game_over:
        DISPLAYSURF.blit(IMGBOX['board'], (0, 0))
        DISPLAYSURF.blit(IMGBOX['player_icon'][turn], (0, 0))
        draw_penguin(center)
        draw_deleted()

        is_clicked = False
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()
            if event.type == MOUSEBUTTONUP:
                is_clicked = True

        block_num = get_block_num_at_pos(mouse_pos)

        if not is_clicked and is_deletable(block_num, center):
            draw_selected(block_num, turn)
        if is_clicked and is_deletable(block_num, center):
            delete_block(block_num)
            turn = next_turn(turn)
            # todo temp
            show_sur_cnt()

        game_over = is_game_over(center)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

    return turn


# 종료 화면
def end_screen(player):
    DISPLAYSURF.blit(IMGBOX['end'][player], (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()
            elif event.type == KEYDOWN or event.type == MOUSEBUTTONUP:
                terminate()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


# 메인 함수
if __name__ == '__main__':
    game_mode = start_screen()
    winner = run_game(game_mode)
    end_screen(winner)

