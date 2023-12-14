# 그리디의 핵심을 나타내는 문제인듯..
## 옛날엔 이 비슷한 문제를 풀었는데 왜 지금은 이 포인트를 생각해내지 못했는가.. (좌절)

import sys

input = sys.stdin.readline

n = int(input())
times = []
for _ in range(n):
    start, end = list(map(int, input().split(" ")))
    times.append([start, end])

times.sort(key = lambda x: (x[1], x[0]))

last = times[0][1]
answer = 1
for time in times[1:]:
    if time[0] >= last:
        last = time[1]
        answer += 1

print(answer)
