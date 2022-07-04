import random
from block import *
from block_control import *


# sur_cnt 백업 배열 반환
def copy_sur_cnt():
    sur_cnt_list = [0]*37
    for i in range(37):
        sur_cnt_list[i] = BLOCKS[i].sur_cnt_

    return sur_cnt_list


# sur_cnt_ 백업으로 덮어쓰기
def paste_sur_cnt(sur_cnt_list):
    for i in range(37):
        BLOCKS[i].sur_cnt_ = sur_cnt_list[i]


# 제거 시뮬레이션, 제거 블록 개수 반환
def delete_block_sim(c_num):
    if c_num == WALL:
        return 0
    elif IS_BLOCK_DELETED[c_num]:
        return 0

    # delete_cen_block
    IS_BLOCK_DELETED[c_num] = True
    BLOCKS[c_num].sur_cnt_ = 0

    # delete_sur_block
    c_surs = BLOCKS[c_num].get_safe_sur_num(IS_BLOCK_DELETED)
    for s_num in c_surs:
        BLOCKS[s_num].sur_cnt_-=1

    del_cnt = 1
    for s_num in c_surs:
        if not is_safe(s_num):
            del_cnt+=delete_block_sim(s_num)
    #print()

    return del_cnt


# 제거 블록 개수 최대인 블록 번호 반환
def get_ai_block_num(p_poses):
    candidate = []
    max_del_cnt = 0

    for i in range(37):
        if not is_deletable(i, p_poses):
            continue

        sur_cnt_copy = copy_sur_cnt()
        deleted_copy = IS_BLOCK_DELETED[:]

        del_cnt = delete_block_sim(i)
        game_over = is_game_over(p_poses)

        paste_sur_cnt(sur_cnt_copy)
        IS_BLOCK_DELETED[:] = deleted_copy[:]

        if game_over:
            continue
        if del_cnt == max_del_cnt:
            candidate.append(i)
        elif del_cnt > max_del_cnt:
            max_del_cnt = del_cnt
            candidate = [i]

    # 아무 블록을 제거해도 게임이 끝날 때
    if not candidate:
        return p_poses[0]
    else:
        return random.choice(candidate)
