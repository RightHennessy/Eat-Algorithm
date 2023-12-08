import sys

input = sys.stdin.readline

n, k = list(map(int, input().split(' ')))

coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

answer = 0
for coin in coins:
    if k//coin > 0:
        answer += (k//coin)
        k %= coin

print(answer)