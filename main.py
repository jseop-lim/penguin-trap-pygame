import pygame, sys
import random
from pygame.locals import *
from game_object import *


def run_game():
    game_over = False
    turn = random.choice([PLAYER1, PLAYER2])

    while not game_over:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(IMGBOX['board'], (0, 0))
        DISPLAYSURF.blit(IMGBOX['player_icon'][turn], (0, 0))
        draw_deleted()

        is_clicked = False
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()
            if event.type == MOUSEBUTTONUP:
                is_clicked = True

        block_num = get_block_num_at_pos(mouse_pos)

        if not is_clicked and is_deletable(block_num):
            draw_selected(block_num, turn)
            draw_skipped(block_num)
        if is_clicked and is_deletable(block_num):
            delete_block(block_num)
            turn = next_turn(turn)

        game_over = is_game_over()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

    return turn


if __name__ == '__main__':
    start_screen()
    winner = run_game()
    end_screen(winner)

