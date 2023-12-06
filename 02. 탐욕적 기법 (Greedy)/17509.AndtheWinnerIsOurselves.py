import sys

input = sys.stdin.readline

solves = []
for _ in range(11):
    solves.append(list(map(int, input().split(' '))))
solves.sort(key = lambda x: x[0])

answer = 0
time = 0
for solve in solves:
    answer += (time + solve[0])
    time += solve[0]
    answer += (solve[1] * 20)

print(answer)