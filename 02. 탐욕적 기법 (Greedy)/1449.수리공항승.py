import sys

input = sys.stdin.readline

n, l = list(map(int, input().split(' ')))
holes = list(map(int, input().split(' ')))
holes.sort()

last = -1
cnt = 0
for hole in holes:
    if last < hole + 0.5:
        cnt += 1
        last = hole - 0.5 + l

print(cnt)