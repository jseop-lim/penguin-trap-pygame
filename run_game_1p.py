from screen import *
from auto import *


# 1인용 엔딩 및 플레이어 아이콘 설정
IMGBOX['end'] = [pygame.image.load('picture/end_p.png'),
                 pygame.image.load('picture/end_c.png')]
IMGBOX['player_icon'] = [pygame.image.load('picture/player_icon.png'),
                         pygame.image.load('picture/computer_icon.png')]


# 플레이어 턴
def player_turn(penguin_poses):
    while(True):
        DISPLAYSURF.blit(IMGBOX['board'], (0, 0))
        DISPLAYSURF.blit(IMGBOX['player_icon'][PLAYER], (0, 0))
        draw_penguin(penguin_poses)
        draw_deleted()

        is_clicked = False
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()
            if event.type == MOUSEBUTTONUP:
                is_clicked = True

        block_num = get_block_num_at_pos(mouse_pos)

        if not is_clicked and is_deletable(block_num, penguin_poses):
            draw_selected(block_num, PLAYER)
        if is_clicked and is_deletable(block_num, penguin_poses):
            delete_block(block_num)
            break

        pygame.display.update()
        FPSCLOCK.tick(FPS)


# 컴퓨터 턴
def computer_turn(penguin_poses):
    block_num = get_ai_block_num(penguin_poses)

    DISPLAYSURF.blit(IMGBOX['board'], (0, 0))
    DISPLAYSURF.blit(IMGBOX['player_icon'][COMPUTER], (0, 0))
    draw_penguin(penguin_poses)
    draw_deleted()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            terminate()

    pygame.display.update()
    pygame.time.delay(100)

    draw_selected(block_num, COMPUTER)
    pygame.display.update()

    pygame.time.delay(650)
    delete_block(block_num)

    pygame.display.update()
    FPSCLOCK.tick(FPS)


# 메인 루프
def run_game(game_mode):
    penguin_num = get_penguin_num(game_mode)
    penguin_poses = get_penguin_poses(game_mode, penguin_num)
    turn = random.choice([PLAYER1, PLAYER2])

    game_over = False
    while not game_over:
        if turn == PLAYER:
            player_turn(penguin_poses)
        else:
            computer_turn(penguin_poses)

        # todo temp
        show_sur_cnt()
        turn = next_turn(turn)
        game_over = is_game_over(penguin_poses)

    return turn


# 메인 함수
if __name__ == '__main__':
    game_mode = start_screen()

    winner = run_game(game_mode)
    pygame.display.update()
    pygame.time.delay(800)

    end_screen(winner)