import pygame, sys
from pygame.locals import *
from game_object import *


def main():
    game_over = False

    while not game_over:

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(IMGBOX['board'], (0, 0))
        draw_deleted()

        is_clicked = False
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()
            if event.type == MOUSEBUTTONDOWN:
                pass
            if event.type == MOUSEBUTTONUP:
                is_clicked = True

        block_num = get_block_num_at_pos(mouse_pos)

        if not is_clicked:
            draw_selected(block_num)
            draw_skipped(block_num)
        if is_clicked:
            delete_block(block_num)

        game_over = is_game_over()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()