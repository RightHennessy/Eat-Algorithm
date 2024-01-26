import sys
input = sys.stdin.readline

answer = []
paper = []
n = int(input())
for i in range(n):
    paper.append(list(map(int, input().split(' '))))

def solution(x, y, m):
    now = paper[x][y]
    for i in range(x, x+m):
        for j in range(y, y+m):
            if now != paper[i][j]:
                solution(x, y, m//2)
                solution(x+m//2, y, m//2)
                solution(x, y+m//2, m//2)
                solution(x+m//2, y+m//2, m//2)
                return
    answer.append(now)

solution(0, 0, n)
print(answer.count(0))
print(answer.count(1))