import pygame, sys
from pygame.locals import *
from block import *


# 전역변수 선언
FPS = 30
WINWIDTH = 600
WINHEIGHT = 600
WHITE = (255, 255, 255)

PLAYER1 = PLAYER = 0
PLAYER2 = COMPUTER = 1

MODE_BASE = 1
MODE_POS = 2
MODE_NUM = 3

# 이미지 로드
IMGBOX = {  'start': pygame.image.load('picture/start.png'),
            'start_text': pygame.image.load('picture/start_text.png'),
            'setting': [pygame.image.load('picture/setting.png'),
                        pygame.image.load('picture/setting_mode1.png'),
                        pygame.image.load('picture/setting_mode2.png'),
                        pygame.image.load('picture/setting_mode3.png')],
            'setting_btn': [pygame.image.load('picture/setting_btn_in.png'),
                            pygame.image.load('picture/setting_btn_out.png')],
            'board': pygame.image.load('picture/board.png'),
            'board_text_pos': pygame.image.load('picture/board_text_pos.png'),
            'board_text_num': pygame.image.load('picture/board_text_num.png'),
            'penguin': pygame.image.load('picture/penguin_cute.png'),
            'selected': [pygame.image.load('picture/selected1.png'),
                         pygame.image.load('picture/selected2.png')],
            'player_icon': [pygame.image.load('picture/player1_icon.png'),
                            pygame.image.load('picture/player2_icon.png')],
            'deleted': pygame.image.load('picture/deleted.png'),
            'skipped': pygame.image.load('picture/skipped.png'),
         }

# key 번호 딕셔너리
K_NUMBOX = {K_1: 1, K_2: 2, K_3: 3,
            K_4: 4, K_5: 5, K_6: 6,
            K_7: 7, K_8: 8, K_9: 9}


# pygame 초기화
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption('남극의 펭귄을 지켜라~!')


# pygame 및 프로그램 종료
def terminate():
    pygame.quit()
    sys.exit()


# 텍스트 깜빡이기
def blink_text(timer, img_name):
    if timer > FPS / 2:
        DISPLAYSURF.blit(IMGBOX[img_name], (0, 0))
        if timer == FPS:
            timer = 0
    timer += 1

    return timer


# 세팅 버튼 위에 마우스 놓였는지 반환
def is_setting_hover(pos):
    x, y = pos
    if 438 <= x <=477 and 523 <= y <= 562:
        return True
    else:
        return False


# 다음턴 사용자 반환
def next_turn(turn):
    if turn == 0:
        return 1
    else:
        return 0


# 블록 위에 마우스 올렸을 때 highlight
def draw_selected(num, player):
    # if not is_deletable(num):
    #     return

    DISPLAYSURF.blit(IMGBOX['selected'][player], BLOCKPOSBOX[num])


# 삭제된 블록에 덧칠
def draw_deleted():
    for num in range(37):
        if IS_BLOCK_DELETED[num]:
            x, y = BLOCKPOSBOX[num]
            DISPLAYSURF.blit(IMGBOX['deleted'], (x-4, y-4.5))


# 펭귄 그리기
def draw_penguin(p_poses):
    PENGUINWID_HALF = PENGUINHEI_HALF = 33
    for p_pos in p_poses:
        x, y = BLOCKPOSBOX[p_pos]
        x = x + BLOCKWID/2 - PENGUINWID_HALF
        y = y + BLOCKHEI/2 - PENGUINHEI_HALF
        DISPLAYSURF.blit(IMGBOX['penguin'], (x, y))


# 좌표로부터 설정번호 반환
def get_setting_num_at_pos(pos):
    SETTEXTWID = 110
    SETTEXTHEI = 19
    SETPOSBOX = [(244, 260), (244, 290), (244, 320)]

    for set_num in range(len(SETPOSBOX)):
        left, top = SETPOSBOX[set_num]
        temp_rect = pygame.Rect(left, top, SETTEXTWID, SETTEXTHEI)
        if temp_rect.collidepoint(pos):
            return set_num + 1

    return 0


# 좌표로부터 블록번호 반환
def get_block_num_at_pos(pos):
    for block_num in range(37):
        left, top = BLOCKPOSBOX[block_num]
        temp_rect = pygame.Rect(left, top+10, BLOCKWID, BLOCKHEI-20)
        if temp_rect.collidepoint(pos):
            return block_num

    return WALL