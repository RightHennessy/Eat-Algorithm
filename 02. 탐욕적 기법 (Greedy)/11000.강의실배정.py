import heapq
import sys
input = sys.stdin.readline

N = int(input())

values = []
for _ in range(N):
    values.append(list(map(int, input().strip().split(' '))))

values.sort(key = lambda x: (x[0], x[1]))
rooms = [0]
heapq.heapify(rooms)

for s, t in values:
    now = rooms[0]
    if s >= now:
        heapq.heappop(rooms)
    heapq.heappush(rooms, t)
print(len(rooms))
