import pygame, sys
from pygame.locals import *
from block import *


#전역변수 선언
FPS = 30
WINWIDTH = 600
WINHEIGHT = 600
WHITE = (255, 255, 255)

PLAYER1 = 0
PLAYER2 = 1

#이미지 로드
IMGBOX = {  'start': pygame.image.load('picture/start.png'),
            'start_text': pygame.image.load('picture/start_text.png'),
            'board': pygame.image.load('picture/board.png'),
            'selected': [pygame.image.load('picture/selected1.png'), pygame.image.load('picture/selected2.png')],
            'player_icon': [pygame.image.load('picture/player1_icon.png'), pygame.image.load('picture/player2_icon.png')],
            'deleted': pygame.image.load('picture/deleted.png'),
            'skipped': pygame.image.load('picture/skipped.png'),
            'end': [pygame.image.load('picture/end1.png'), pygame.image.load('picture/end2.png')]
         }

#pygame 초기화
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption('남극의 펭귄을 지켜라~!')


#시작화면 출력
def start_screen():
    timer = 0

    while True:
        DISPLAYSURF.blit(IMGBOX['start_text'], (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()
            elif event.type == KEYDOWN or event.type == MOUSEBUTTONUP:
                return

        #텍스트 깜박이기
        if timer > FPS/2:
            DISPLAYSURF.blit(IMGBOX['start'], (0, 0))
            if timer == FPS:
                timer = 0
        timer +=1

        pygame.display.update()
        FPSCLOCK.tick(FPS)


#pygame 및 프로그램 종료
def terminate():
    pygame.quit()
    sys.exit()


#블록이 제거가능한지 판단
def is_deletable(num):
    if num==WALL or num==CENTER or IS_BLOCK_DELETED[num]:
        return False
    else:
        return True


#다음턴 사용자 반환
def next_turn(turn):
    if turn == 0:
        return 1
    else:
        return 0


#게임 종료 조건 확인
def is_game_over():
    if IS_BLOCK_DELETED[CENTER]:
        return True
    else:
        return False


#블록 위에 마우스 올렸을 때 highlight
def draw_selected(num, player):
    # if not is_deletable(num):
    #     return

    DISPLAYSURF.blit(IMGBOX['selected'][player], BLOCKPOSBOX[num])


#삭제된 블록에 덧칠
def draw_deleted():
    for num in range(37):
        if IS_BLOCK_DELETED[num]:
            x, y = BLOCKPOSBOX[num]
            DISPLAYSURF.blit(IMGBOX['deleted'], (x-4, y-4.5))


# TODO
#스킵된 블록 덧칠
def draw_skipped(num):
    # if not is_deletable(num):
    #     return

    for i in range(6):
        if BLOCKS[num].surs_[i].skipped_:
            s = BLOCKS[num].surs_[i].num_
            if s != WALL and not IS_BLOCK_DELETED[s]:
                x, y = BLOCKPOSBOX[s]
                DISPLAYSURF.blit(IMGBOX['skipped'], (x - 4, y - 4.5))


#블록 지우기 연산
def delete_block(cen_num):
    # if not is_deletable(num):
    #     return

    #delete_cen_block
    IS_BLOCK_DELETED[cen_num] = True

    #delete_sur_block
    for sur_num in BLOCKS[cen_num].get_surs_num_list():
        BLOCKS[sur_num].check_skip()
        if not BLOCKS[sur_num].is_safe():
            IS_BLOCK_DELETED[sur_num] = True


#좌표로부터 블록번호 반환
def get_block_num_at_pos(pos):
    for block_num in range(37):
        left, top = BLOCKPOSBOX[block_num]
        temp_rect = pygame.Rect(left, top+10, BLOCKWID, BLOCKHEI-20)
        if temp_rect.collidepoint(pos):
            return block_num

    return WALL


#게임 종료화면
def end_screen(player):
    while True:
        DISPLAYSURF.blit(IMGBOX['end'][player], (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()
            elif event.type == KEYDOWN or event.type == MOUSEBUTTONUP:
                terminate()

        pygame.display.update()
        FPSCLOCK.tick(FPS)
