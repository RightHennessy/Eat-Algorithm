# 시간초과 -> 삼각수 합을 1000번 index까지 미리구해둬서..
## -> 삼각수가 1000이하인 44번까지만 미리 만들어두면 된다고 ~

import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

nums = []
for i in range(1,45):
    nums.append(i*(i+1)//2)
num_max = 44

ans = []
n = int(input())
for idx in range(n):
    m = int(input())
    for i in range(num_max):
        for j in range(i, num_max):
            for k in range(j, num_max):
                if nums[i] >= m :
                    ans.append(0)
                    break
                elif nums[i] + nums[j] + nums[k] == m:
                    ans.append(1)
                    break
            if len(ans) > idx:
                break
        if len(ans) > idx:
                break

for a in ans:
    print(a)
    