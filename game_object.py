import pygame, sys
from pygame.locals import *
from block import *

#전역변수 선언
FPS = 30
WINWIDTH = 600
WINHEIGHT = 600
WHITE = (255, 255, 255)

#이미지 로드
IMGBOX = {  'board': pygame.image.load('picture/board.png'),
            'selected': pygame.image.load('picture/selected.png'),
            'deleted': pygame.image.load('picture/deleted.png'),
            'skipped': pygame.image.load('picture/skipped.png')
         }

#pygame 초기화
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption('남극의 펭귄을 지켜라~!')


#pygame 및 프로그램 종료
def terminate():
    pygame.quit()
    sys.exit()

#블록 위에 마우스 올렸을 때 highlight
def draw_selected(num):
    if num!=WALL and num!=CENTER and not IS_BLOCK_DELETED[num]:
        DISPLAYSURF.blit(IMGBOX['selected'], BLOCKPOSBOX[num])

#삭제된 블록에 덧칠
def draw_deleted():
    for num in range(37):
        if IS_BLOCK_DELETED[num]:
            x, y = BLOCKPOSBOX[num]
            DISPLAYSURF.blit(IMGBOX['deleted'], (x-4, y-4.5))

# TODO 임시적
#스킵된 블록 덧칠
def draw_skipped(num):
    if num!=WALL and num!=CENTER and not IS_BLOCK_DELETED[num]:
        for i in range(6):
            if BLOCKS[num].surs_[i].skipped_:
                s = BLOCKS[num].surs_[i].num_
                if s != WALL and not IS_BLOCK_DELETED[s]:
                    x, y = BLOCKPOSBOX[s]
                    DISPLAYSURF.blit(IMGBOX['skipped'], (x - 4, y - 4.5))

#게임 종료 조건 확인
def is_game_over():
    if IS_BLOCK_DELETED[CENTER]:
        return True
    else:
        return False

def delete_block(cen_num):
    if cen_num==WALL or cen_num==CENTER or IS_BLOCK_DELETED[cen_num]:
        return

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

