import sys
input = sys.stdin.readline

ans = 0
tries = []
for _ in range(11):
    T, V = list(map(int, input().strip().split(' ')))
    tries.append([T, V])

# index 0번으로 정렬
tries.sort(key=lambda x: x[0])
time = 0
for i in range(11):
    t, v = tries[i]
    ans += (t + 20*v + time)
    time += t
print(ans)
