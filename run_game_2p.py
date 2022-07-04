from screen import *


IMGBOX['end'] = [pygame.image.load('picture/end_p1.png'),
                 pygame.image.load('picture/end_p2.png')]


# 메인 루프
def run_game(game_mode):
    penguin_num = get_penguin_num(game_mode)
    penguin_poses = get_penguin_poses(game_mode, penguin_num)
    turn = random.choice([PLAYER1, PLAYER2])

    game_over = False
    while not game_over:
        DISPLAYSURF.blit(IMGBOX['board'], (0, 0))
        DISPLAYSURF.blit(IMGBOX['player_icon'][turn], (0, 0))
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
            draw_selected(block_num, turn)
        if is_clicked and is_deletable(block_num, penguin_poses):
            delete_block(block_num)
            turn = next_turn(turn)
            # todo temp
            show_sur_cnt()

        game_over = is_game_over(penguin_poses)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

    return turn


# 메인 함수
if __name__ == '__main__':
    game_mode = start_screen()

    winner = run_game(game_mode)
    pygame.display.update()
    pygame.time.delay(800)

    end_screen(winner)