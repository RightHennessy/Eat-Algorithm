import sys
input = sys.stdin.readline

ans = 0
N = int(input())

values = []
for _ in range(N):
    values.append(list(map(int, input().strip().split(' '))))

# 아마 시작, 끝이 같은 경우가 있을듯
values.sort(key = lambda x: (x[1], x[0]))

time = 0
for i in range(N):
    if time <= values[i][0]:
        ans += 1
        time = values[i][1]
print(ans)
