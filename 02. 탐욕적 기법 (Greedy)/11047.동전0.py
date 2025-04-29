import sys
input = sys.stdin.readline

ans = 0
N, K = list(map(int, input().strip().split(' ')))

values = []
for _ in range(N):
    values.append(int(input()))

for i in range(N-1, -1, -1):
    if values[i] <= K:
        ans += K//values[i]
        K %= values[i]
print(ans)
