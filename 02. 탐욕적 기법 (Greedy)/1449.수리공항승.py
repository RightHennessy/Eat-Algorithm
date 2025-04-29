import sys
input = sys.stdin.readline

N, L = list(map(int, input().strip().split(' ')))
holes = list(map(int, input().strip().split(' ')))
holes.sort()

ans = 1
now = holes[0] + L - 1
for i in range(1, len(holes)):
    if holes[i] > now:
        ans += 1
        now = holes[i] + L -1
print(ans)
