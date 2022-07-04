from block_control import *
from auto import *

if __name__ == '__main__':
    # 지워진 블록 다시 순회 -> SOLVED!
    # delete_seq = [4, 10, 9, 0, 2, 6, 5, 8, 7, 20, 21, 33, 32]

    # 블록 섬 -> SOLVED!
    # delete_seq = [13, 20, 26, 31, 35, 29, 23, 16, 10]
    '''
    # 벽 때문에 산다
    delete_seq = [28, 29, 17, 24, 30, 10, 9, 15]

    for i in delete_seq:
        delete_block(i)
        show_sur_cnt()
    '''
    #delete_block(20)
    arr = []
    for i in range(37):
        ai = get_ai_block_num([CENTER])
        #print(IS_BLOCK_DELETED)
        #print("\nai_block_num:", ai)
        #delete_block(int(ai))
        arr.append(ai)
        delete_block(ai)
        show_sur_cnt()
        if is_game_over([CENTER]):
            break

    print(arr)