# 이 문제가 왜 분할정복이지..? 
## 알고보면 대놓고 분할정복이다 ~

### pow vs math.pow 차이점

import sys
input = sys.stdin.readline

def solution(a, b, c):
    if b==1:
        return a % c
    elif b==2:
        return a**2 % c
    elif b%2 == 0:
        return solution(a, b//2, c)**2 % c
    elif b%2 != 0:
        return solution(a, b//2, c)**2*a % c

a, b, c = list(map(int, input().split(' ')))
print(solution(a%c, b, c))