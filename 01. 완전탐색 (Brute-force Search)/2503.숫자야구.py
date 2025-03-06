import sys
from itertools import permutations

input = sys.stdin.readline
nums = [x for x in range(1,10)]
cases = permutations(nums, 3)
tries = []

def solution():
    global cases
    N = int(input())
    for _ in range(N):
        # 0:num 1:strike 2:ball
        tries.append(list(map(int, input().split(' '))))

    for t in tries:
        number = list(map(int, str(t[0])))
        tmp = []
        for c in cases:
            if check(c, number) == (t[1], t[2]):
                tmp.append(c)
        cases = tmp

    print(len(cases))
    return

def check(a, b):
    strike_count = 0
    ball_count = 0 
    for i in range(3):
        if a[i] == b[i]: strike_count += 1
        elif a[i] in b: ball_count += 1
    return (strike_count, ball_count)

solution()