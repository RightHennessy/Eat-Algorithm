# 문제를 잘 읽자...'연속된~'

import sys

input = sys.stdin.readline

board = []
n = int(input())
for _ in range(n):
    board.append(list(input().strip()))

answer = 0
for i in range(n):
    prev = board[i][0]
    tmp = 1
    for j in range(1, n):
        if board[i][j] == prev:
            tmp += 1
        else:
            prev = board[i][j]
            answer = max(answer, tmp)
            tmp = 1
    answer = max(answer, tmp)

for i in range(n):
    prev = board[0][i]
    tmp = 1
    for j in range(1, n):
        if board[j][i] == prev:
            tmp += 1
        else:
            prev = board[j][i]
            answer = max(answer, tmp)
            tmp = 1
    answer = max(answer, tmp)

cases = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(n):
    for j in range(n):
        for case in cases:
            if i+case[0] == -1 or i+case[0] == n or j+case[1] == -1 or j+case[1] == n:
                continue
            if board[i+case[0]][j+case[1]] == board[i][j]:
                continue
            board[i][j], board[i+case[0]][j+case[1]] = board[i+case[0]][j+case[1]], board[i][j]
            # 가로 확인
            prev = board[i][0]
            tmp = 1
            for k in range(1, n):
                if board[i][k] == prev:
                    tmp += 1
                else:
                    prev = board[i][k]
                    answer = max(answer, tmp)
                    tmp =1
            answer = max(answer, tmp)
            # 세로 확인
            prev = board[0][j]
            tmp = 1
            for k in range(1, n):
                if board[k][j] == prev:
                    tmp += 1
                else:
                    prev = board[k][j]
                    answer = max(answer, tmp)
                    tmp =1
            answer = max(answer, tmp)
            board[i+case[0]][j+case[1]], board[i][j] = board[i][j], board[i+case[0]][j+case[1]]

print(answer)