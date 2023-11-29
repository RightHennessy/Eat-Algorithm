import sys

input = sys.stdin.readline

n = int(input())
answer = 0
for i in range(1, n+1):
    if i + sum(list(map(int, list(str(i))))) == n:
        answer = i
        break
print(answer)
    