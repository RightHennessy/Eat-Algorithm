import sys
from itertools import combinations

input = sys.stdin.readline

N, M = list(map(int, input().split(' ')))
nums = list(map(int, input().split(' ')))

ans = 0

for i in range(1, N+1):
    cases = combinations(nums, i)
    for c in cases:
        if sum(c) == M:
            ans += 1

print(ans)