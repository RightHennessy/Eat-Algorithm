import sys
from collections import deque 

input = sys.stdin.readline

n, k = [int(x) for x in input().split(' ')]

items = input().strip().split(' ')
now = set()
dic = dict()

for idx, item in enumerate(items):
    try:
        dic[item].append(idx)
    except:
        dic[item] = deque([idx])



count = 0
for item in items:
    temp = [0, 0]
    if item in now:
        dic[item].popleft()
    elif len(now) <n:
        now.add(item)
        dic[item].popleft()
    elif len(now) == n:
        for x in now:
            try:
                if temp[1] < dic[x][0]:
                    temp = [x, dic[x][0]]
            except:
                temp = [x, -1]
                break
        count += 1
        now.remove(temp[0])
        now.add(item)
        dic[item].popleft()

print(count)
