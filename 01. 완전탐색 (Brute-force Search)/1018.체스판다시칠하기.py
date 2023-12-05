# 보드판은 B로 시작할수도, W로 시작할수도..
## 꽤나 빡구현으로 풀었다.. 나쁘지 않아... 
## 생각을 코드로 옮기는 연습을 더 해야할듯 ㅜㅅㅜ

import sys
from collections import deque 

input = sys.stdin.readline

chess = ['WBWBWBWB', 'BWBWBWBW']*4
chess = [list(x) for x in chess]
n, m = list(map(int, input().split(' ')))
board = []
change = 64
for _ in range(n):
    board.append(list(input().strip()))

for i in range(n-7):
    top = board[i][0]
    count = deque([0])
    for l in range(7):
        cnt = 0
        for k in range(i, i+8):
            if board[k][l] != chess[k-i][l]:
                cnt += 1
        count.append(cnt)

    for j in range(m-7):
        count.popleft()
        cnt = 0
        for k in range(i, i+8):
            if board[k][j+7] != chess[k-i][(j+7)%8]:
                cnt += 1
        count.append(cnt)
        total = sum(count)
        change = min(min(total, 64-total), change)
print(change)