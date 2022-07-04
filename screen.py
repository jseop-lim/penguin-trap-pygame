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


# 펭귄 개수 반환
def get_penguin_num(mode):
    if mode < MODE_NUM:
        return 1

    timer = 0
    while True:
        DISPLAYSURF.blit(IMGBOX['board_text_num'], (0, 0))
        timer = blink_text(timer, 'board')

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()
            elif event.type == KEYDOWN:
                if event.key in K_NUMBOX:
                    return K_NUMBOX[event.key]

        pygame.display.update()
        FPSCLOCK.tick(FPS)


# 펭귄 위치 반환
def get_penguin_poses(mode, p_num):
    if mode < MODE_POS:
        return [CENTER]

    p_poses = []
    timer = 0
    while len(p_poses) < p_num:
        DISPLAYSURF.blit(IMGBOX['board_text_pos'], (0, 0))
        timer = blink_text(timer, 'board')
        draw_penguin(p_poses)
        is_clicked = False
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()
            elif event.type == MOUSEBUTTONUP:
                is_clicked = True

        block_num = get_block_num_at_pos(mouse_pos)

        if block_num != WALL and block_num not in p_poses:
            if is_clicked:
                p_poses.append(block_num)
            else:
                draw_penguin([block_num])

        pygame.display.update()
        FPSCLOCK.tick(FPS)

    return p_poses


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


