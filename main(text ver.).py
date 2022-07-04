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

    #delete_seq = [4, 25, 19, 27, 6, 5, 30, 32, 34, 36, 21, 8, 3, 33, 9, 0, 2, 29, 15, 28, 22, 18]
    #delete_seq = [32, 33, 19, 14, 8, 35, 21, 15, 16, 9, 23, 34, 0, 6, 36, 2, 28, 3, 1]
    delete_seq = [7, 3, 35, 23, 24, 16, 34, 15, 6, 4, 33, 28, 8, 1, 21, 36, 2, 32, 27, 0]
    for i in delete_seq:
        delete_block(i)
        show_sur_cnt()