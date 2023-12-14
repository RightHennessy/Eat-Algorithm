# heapq.. 파이썬 왤케 잘만들어 놨는데 ~

import sys
import heapq

input = sys.stdin.readline

n = int(input())
times = []
for _ in range(n):
    start, end = list(map(int, input().split(" ")))
    times.append([start, end])

times.sort(key = lambda x: (x[0], x[1]))

time_line = [times[0][1]]

for time in times[1:]:
    if time[0] >= time_line[0]:
        heapq.heappop(time_line)
    heapq.heappush(time_line, time[1])


print(len(time_line))