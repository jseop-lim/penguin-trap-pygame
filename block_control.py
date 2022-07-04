from block import *
from render import *

# 블록이 제거가능한지 판단
def is_deletable(num, p_poses):
    if num==WALL or num in p_poses or IS_BLOCK_DELETED[num]:
        return False
    else:
        return True


# 게임 종료 조건 확인
def is_game_over(p_poses):
    for p_pos in p_poses:
        if IS_BLOCK_DELETED[p_pos]:
            return True
    else:
        return False


# 블록 지우기 연산
def delete_block(c_num):
    # if not is_deletable(num):
    #     return
    # todo temp
    print()

    if c_num == WALL:
        return
    elif IS_BLOCK_DELETED[c_num]:
        return

    # todo temp
    print('%d' %c_num, end=', ')

    # delete_cen_block
    IS_BLOCK_DELETED[c_num] = True
    BLOCKS[c_num].sur_cnt_ = 0
    draw_delete_temp(c_num)

    # delete_sur_block
    c_surs = BLOCKS[c_num].get_safe_sur_num(IS_BLOCK_DELETED)
    for s_num in c_surs:
        BLOCKS[s_num].sur_cnt_-=1

    for s_num in c_surs:
        if not is_safe(s_num):
            delete_block(s_num)
    #todo temp
    print()


# 한 블록의 어그러짐 정도 합 반환
def get_net_force(c_num):
    net_f = 0

    c_f = WEIGHT / BLOCKS[c_num].sur_cnt_
    for s_num in BLOCKS[c_num].get_safe_sur_num(IS_BLOCK_DELETED):
        s_f = WEIGHT / BLOCKS[s_num].sur_cnt_
        net_f += abs(c_f - s_f)

    w_num = BLOCKS[c_num].surs_.count(WALL)

    if c_f == 20:
        net_f += 3
    if w_num == 2:
        net_f += 3
    elif w_num == 1:
        net_f += 2

    # todo temp
    # print('<%d>' % BLOCKS[c_num].surs_.count(WALL), end='')
    # print('(%d) - ' %net_f, end='')


    return net_f


# todo temp
# 모든 블록의 sur_cnt_ 출력
def show_sur_cnt():
    print(end='     ')
    for i in range(0, 3):
        print(BLOCKS[i].sur_cnt_, end=' ')
    print(); print(end='  ')
    for i in range(3, 9):
        print(BLOCKS[i].sur_cnt_, end=' ')
    print(); print(end=' ')
    for i in range(9, 15):
        print(BLOCKS[i].sur_cnt_, end=' ')
    print(); print(end='')
    for i in range(15, 22):
        print(BLOCKS[i].sur_cnt_, end=' ')
    print(); print(end=' ')
    for i in range(22, 28):
        print(BLOCKS[i].sur_cnt_, end=' ')
    print(); print(end='')
    for i in range(28, 34):
        print(BLOCKS[i].sur_cnt_, end=' ')
    print(); print(end='   ')
    for i in range(34, 37):
        print(BLOCKS[i].sur_cnt_, end=' ')
    print(); print()


# 블록 생존여부 반환
def is_safe(c_num):
    # todo temp
    # print(c_num, end='')
    # 지워진 블록을 다시 순회
    # todo modified
    if BLOCKS[c_num].sur_cnt_ <= 2:
        return False
    # 블록주변에 벽만 존재
    elif not BLOCKS[c_num].is_wall_safe(IS_BLOCK_DELETED):
        return False
    # 일반적 경우(블록 존재)
    elif get_net_force(c_num) > THRESHOLD:
        return False
    else:
        return True
