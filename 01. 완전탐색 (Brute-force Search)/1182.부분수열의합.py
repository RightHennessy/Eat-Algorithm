# 뭐여.. 완전 탐색 문제 중에 제일 쉬웠던 문제.. 이게 맞나?

import sys
from itertools import combinations

input = sys.stdin.readline
n, s = list(map(int, input().split(' ')))
nums = list(map(int, input().split(' ')))

cases = []
for i in range(1, n+1):
    cases += combinations(nums, i)

answer = 0
for case in cases:
    if sum(case) == s:
        answer += 1

print(answer)