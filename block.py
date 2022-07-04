class SurBlock:
    def __init__(self, num, force=0):
        self.num_ = num
        self.force_ = force
        self.skipped_ = False

    def __str__(self):
        print(self.num_, end='')


class CenBlock:
    def __init__(self, num, surs):
        self.num_ = num
        # self.deleted_ = False
        self.surs_ = []
        for sur in surs:
            self.surs_.append(SurBlock(sur))

    def __str__(self):
        show = ''
        show+='%2d ' % self.num_
        show+='['
        for sur in self.surs_:
            show+='%2d ' % sur.num_
        show+='] '
        return show

    # def delete(self):
    #     self.deleted_ = True
    # def get_sur_num(self, num):
    #     return self.surs_[num].num_

    def get_surs_num_list(self):
        surs_num_list = []
        for i in range(6):
            sur_num = self.surs_[i].num_
            if sur_num != WALL:
                surs_num_list.append(sur_num)
        return surs_num_list

    def check_skip(self):
        for rel_num in range(3):
            if IS_BLOCK_DELETED[self.surs_[rel_num].num_]:
                self.surs_[rel_num+3].skipped_ = True
        for rel_num in range(3, 6):
            if IS_BLOCK_DELETED[self.surs_[rel_num].num_]:
                self.surs_[rel_num-3].skipped_ = True

    def is_safe(self):
        this_case = [False]*6
        for num in range(6):
            sur_block = self.surs_[num]
            if not sur_block.skipped_ and not IS_BLOCK_DELETED[sur_block.num_]:
                return True
            if not IS_BLOCK_DELETED[sur_block.num_]:
                this_case[num] = True
        safe_case = [[True, False, True, False, True, False], [False, True, False, True, False, True]]
        if this_case in safe_case:
            return True
        return False


########################################################################

#블록 번호 관련 전역변수
WALL = 37
CENTER = 18
WEIGHT = 10
BLOCKS = []

IS_BLOCK_DELETED = [False] * 38

#블록 절대번호 상대번호 입력
BLOCKS.append(CenBlock(0, [WALL, WALL, 1, 5, 4, WALL]))
BLOCKS.append(CenBlock(1, [WALL, WALL, 2, 6, 5, 0]))
BLOCKS.append(CenBlock(2, [WALL, WALL, WALL, 7, 6, 1]))
BLOCKS.append(CenBlock(3, [WALL, WALL, 4, 10, 9, WALL]))
BLOCKS.append(CenBlock(4, [WALL, 0, 5, 11, 10, 3]))
BLOCKS.append(CenBlock(5, [0, 1, 6, 12, 11, 4]))
BLOCKS.append(CenBlock(6, [1, 2, 7, 13, 12, 5]))
BLOCKS.append(CenBlock(7, [2, WALL, 8, 14, 13, 6]))
BLOCKS.append(CenBlock(8, [WALL, WALL, WALL, WALL, 14, 7]))
BLOCKS.append(CenBlock(9, [WALL, 3, 10, 16, 15, WALL]))
s10 = [3, 4, 11, 17, 16, 9]
for i in range(4):
    BLOCKS.append(CenBlock(i + 10, s10))
    for j in range(len(s10)):
        s10[j]+=1
BLOCKS.append(CenBlock(14, [7, 8, WALL, 21, 20, 13]))
BLOCKS.append(CenBlock(15, [WALL, 9, 16, 22, WALL, WALL]))
s16 = [9, 10, 17, 23, 22, 15]
for i in range(5):
    BLOCKS.append(CenBlock(i + 16, s16))
    for j in range(len(s16)):
        s16[j]+=1
BLOCKS.append(CenBlock(21, [14, WALL, WALL, WALL, 27, 20]))
BLOCKS.append(CenBlock(22, [15, 16, 23, 29, 28, WALL]))
s23 = [16, 17, 24, 30, 29, 22]
for i in range(4):
    BLOCKS.append(CenBlock(i + 23, s23))
    for j in range(len(s23)):
        s23[j]+=1
BLOCKS.append(CenBlock(27, [20, 21, WALL, WALL, 33, 26]))
BLOCKS.append(CenBlock(28, [WALL, 22, 29, WALL, WALL, WALL]))
BLOCKS.append(CenBlock(29, [22, 23, 30, 34, WALL, 28]))
BLOCKS.append(CenBlock(30, [23, 24, 31, 35, 34, 29]))
BLOCKS.append(CenBlock(31, [24, 25, 32, 36, 35, 30]))
BLOCKS.append(CenBlock(32, [25, 26, 33, WALL, 36, 31]))
BLOCKS.append(CenBlock(33, [26, 27, WALL, WALL, WALL, 32]))
BLOCKS.append(CenBlock(34, [29, 30, 35, WALL, WALL, WALL]))
BLOCKS.append(CenBlock(35, [30, 31, 36, WALL, WALL, 34]))
BLOCKS.append(CenBlock(36, [31, 32, WALL, WALL, WALL, 35]))


#블록 좌표 관련 전역변수
BLOCKWID = 69
BLOCKHEI = 80
BLOCKWIDGAP = 73.2
BLOCKHEIGAP = 63.4

FIRSTBLOCKPOS = (228, 69)
THIRDBLOCKPOS = (118.5, 133)
BLOCKPOSBOX = []

#블록 좌표 입력
white_pos = list(FIRSTBLOCKPOS)
blue_pos = list(THIRDBLOCKPOS)

for i in range(0, 3):
    BLOCKPOSBOX.append(tuple(white_pos))
    white_pos[0]+=BLOCKWIDGAP
white_pos[0]-=BLOCKWIDGAP*5
white_pos[1]+=BLOCKHEIGAP*2

for i in range(3, 9):
    BLOCKPOSBOX.append(tuple(blue_pos))
    blue_pos[0]+=BLOCKWIDGAP
blue_pos[0]-=BLOCKWIDGAP*7
blue_pos[1]+=BLOCKHEIGAP*2

for i in range(9, 15):
    BLOCKPOSBOX.append(tuple(white_pos))
    white_pos[0]+=BLOCKWIDGAP
white_pos[0]-=BLOCKWIDGAP*6
white_pos[1]+=BLOCKHEIGAP*2

for i in range(15, 22):
    BLOCKPOSBOX.append(tuple(blue_pos))
    blue_pos[0]+=BLOCKWIDGAP
blue_pos[0]-=BLOCKWIDGAP*7
blue_pos[1]+=BLOCKHEIGAP*2

for i in range(22, 28):
    BLOCKPOSBOX.append(tuple(white_pos))
    white_pos[0]+=BLOCKWIDGAP
white_pos[0]-=BLOCKWIDGAP*5
white_pos[1]+=BLOCKHEIGAP*2

for i in range(28, 34):
    BLOCKPOSBOX.append(tuple(blue_pos))
    blue_pos[0]+=BLOCKWIDGAP

for i in range(34, 37):
    BLOCKPOSBOX.append(tuple(white_pos))
    white_pos[0]+=BLOCKWIDGAP