class CenBlock:
    def __init__(self, num, surs, sur_cnt=6):
        self.num_ = num
        self.surs_ = surs
        self.sur_cnt_ = sur_cnt

    def get_safe_sur_num(self, deleted_list):
        safe_surs = []
        for s_num in self.surs_:
            if s_num == WALL:
                continue
            elif deleted_list[s_num]:
                continue
            else:
                safe_surs.append(s_num)

        return safe_surs

    def is_wall_safe(self, deleted_list):
        for s_num in self.surs_:
            if s_num == WALL:
                continue
            elif deleted_list[s_num]:
                continue
            else:
                return True

        if self.sur_cnt_ > 2:
            return True
        else:
            return False

# TODO 에라 모르겠
'''

1단계
1. cen 삭제
2. surs 돌면서 cen 주변 6개 force 계산 -> CenBlock에 surs.force_ 계산하는 함수(쉬움), CenBlock surs 개수 계산 함수
3. surs 돌면서 블록 제거가능한지 계산 -> CenBlock에 surs.force_ 합력 계산하는 함수, 역치랑 비교하는 함수(리스트 반환)
4. 제거가능한거 한꺼번에 제거 -> CenBlock에 surs 돌면서 리스트 True인거 제거

2단계
-> 1단계 순서 2~4 각 sur들에 대해 ㄱㄱ

delta_f: (없어진 블록 땜시 분배해줘야 되는 힘) / (현재 블록수)
defta_f는 sur_b 들이 가지는 값
처음 빠진거 주변 블록 사이 경계는 등비 합 구하고 나머지는 delta씩 더해줌
주변 6개 돌면서 is_safe() 

====일단 여기까지 짜는걸로ㅇㅇ====
빠지면 그 블록 주위로 재귀적
깊이는??? ㅁㄹ
'''

########################################################################

# 블록 번호 관련 전역변수
WALL = 37
CENTER = 18
BLOCKS = []

# 블록 삭제 관련 전역변수
IS_BLOCK_DELETED = [False]*38
WEIGHT = 60 # (= 1~6 최소공배수)
# todo modified
THRESHOLD = 17

# 블록 절대번호 상대번호 입력
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
    BLOCKS.append(CenBlock(i + 10, s10[:]))
    for j in range(len(s10)):
        s10[j]+=1
BLOCKS.append(CenBlock(14, [7, 8, WALL, 21, 20, 13]))
BLOCKS.append(CenBlock(15, [WALL, 9, 16, 22, WALL, WALL]))
s16 = [9, 10, 17, 23, 22, 15]
for i in range(5):
    BLOCKS.append(CenBlock(i + 16, s16[:]))
    for j in range(len(s16)):
        s16[j]+=1
BLOCKS.append(CenBlock(21, [14, WALL, WALL, WALL, 27, 20]))
BLOCKS.append(CenBlock(22, [15, 16, 23, 29, 28, WALL]))
s23 = [16, 17, 24, 30, 29, 22]
for i in range(4):
    BLOCKS.append(CenBlock(i + 23, s23[:]))
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

# 블록 좌표 관련 전역변수
BLOCKWID = 69
BLOCKHEI = 80
BLOCKWIDGAP = 73.2
BLOCKHEIGAP = 63.4

FIRSTBLOCKPOS = (228, 69)
THIRDBLOCKPOS = (118.5, 133)
BLOCKPOSBOX = []

# 블록 좌표 입력
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


if __name__ ==  "__main__":
    for i in range(37):
        print(i, BLOCKS[i].num_, BLOCKS[i].surs_)