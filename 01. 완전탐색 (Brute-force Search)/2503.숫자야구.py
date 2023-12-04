# 틀렸던 이유 : 마지막 원소 판단 기준...
# -> 똑같은 조건이 두번 들어오면 2번 추가함.. 이런..
# 해결 : 1. 앞으로는 마지막 원소 판단을 idx로 하던지 2. 정답을 set으로 만들자(중복 제거 확실히)

import sys
from itertools import permutations

def compare(x, y):
    strike = 0
    ball = 0
    for i in range(3):
        if x[i] == y[i]:
            strike += 1
        elif x[i] in y:
            ball += 1
    return strike, ball

input = sys.stdin.readline

n = int(input())
games = []
cases = permutations([x for x in range(1, 10)], 3)
ans = []

for _ in range(n):
    games.append(list(map(int, input().split(' '))))

for item in cases:
    for idx, game in enumerate(games):
        if (game[1], game[2]) != compare(list(item), list(map(int, list(str(game[0]))))):
            break
        if idx + 1 == len(games):
            ans.append(item)

print(len(ans))
