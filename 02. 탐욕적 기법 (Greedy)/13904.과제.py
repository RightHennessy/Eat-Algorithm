# 그래도 셀프 해결한.. ㅋㅋ
## 뒤에서부터 읽어야하는 대표적인 문제이다!

import sys
input = sys.stdin.readline

def solution(assingments):
    max_date = 0
    dic = dict()
    temp = []
    for date, score in assingments:
        if max_date < date:
            max_date = date
        if date in dic:
            dic[date].append(score)
        else:
            dic[date] = [score]

    answer = 0
    for i in reversed(range(1, max_date+1)):
        if i in dic:
            now = sorted(dic[i])
            if temp:
                max_temp = max(temp)
                if now[-1] < max_temp:
                    answer += max_temp
                    temp.remove(max_temp)
                    temp.extend(now)
                else:
                    answer += now[-1]
                    temp.extend(now[:-1])
            else:
                answer += now[-1]
                temp.extend(now[:-1])
        else:
            if temp:
                max_temp = max(temp)
                answer += max_temp
                temp.remove(max_temp)
    return answer

n = int(input())
assingments = []
for i in range(n):
    assingments.append([int(x) for x in input().split(' ')])
print(solution(assingments))