# 함부로 중복값을 제거하지 말자 !!

from collections import deque
import sys

input = sys.stdin.readline

def solution(n, k,sensors):
    distance = []
    for i in range(0, n-1):
        distance.append(sensors[i+1] - sensors[i])
    distance.sort(reverse=True)

    return sum(distance[k-1:])

n = int(input())
k = int(input())
sensors = sorted([int(x) for x in input().split(' ')])

print(solution(n, k, sensors))
