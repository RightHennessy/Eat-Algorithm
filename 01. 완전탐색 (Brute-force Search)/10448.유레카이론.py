from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

T = []
s = 0
for i in range(1,500):
    s += i
    if s > 1000:
        break
    T.append(s)

cases = combinations_with_replacement(T, 3)
ans = [0 for _ in range(1001)]
for c in cases:
    tmp = sum(c)
    if tmp <= 1000:
        ans[tmp] = 1

N = int(input())
for _ in range(N):
    print(ans[int(input())])