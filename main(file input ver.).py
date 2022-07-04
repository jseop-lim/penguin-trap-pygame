from game_object import *

if __name__ == '__main__':
    delete_seq = [4, 10, 9, 0, 2, 6, 5, 8, 7, 20, 21, 33, 32]
    for i in delete_seq:
        delete_block(i)
        show_sur_cnt()
