import sys
input = sys.stdin.readline

answer = []
paper = []
n = int(input())
for i in range(n):
    paper.append(list(map(int, input().split(' '))))
base = 3

def solution(x, y, m):
    now = paper[x][y]
    for i in range(x, x+m):
        for j in range(y, y+m):
            if now != paper[i][j]:
                size = m//base
                for k in range(base):
                    for l in range(base):
                        solution(x+size*k, y+size*l, size)
                return
    answer.append(now)

solution(0, 0, n)
print(answer.count(-1))
print(answer.count(0))
print(answer.count(1))