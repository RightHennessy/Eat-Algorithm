import sys

input = sys.stdin.readline

answers = []
while True:
    l, p, v = list(map(int, input().split(' ')))
    if l == 0 and p == 0 and v == 0:
        break

    cnt = 0
    while v > p:
        cnt += l
        v -= p
    cnt += min(l, v)
    answers.append(cnt)

for idx, answer in enumerate(answers):
    print('Case %d: %d' %(idx+1, answer))