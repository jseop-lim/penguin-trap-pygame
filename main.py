# 플레이어 수 입력 및 실행
if __name__ == '__main__':
    player_num = 100
    while player_num<-1 or player_num>2:
        player_num = int(input('플레이어 수 입력(-1은 종료): '))

    if player_num != -1:
        if player_num == 0:
            from run_game_0p import *
        elif player_num == 1:
            from run_game_1p import *
        else:
            from run_game_2p import *

        game_mode = start_screen()
        winner = run_game(game_mode)
        pygame.display.update()
        pygame.time.delay(800)
        end_screen(winner)