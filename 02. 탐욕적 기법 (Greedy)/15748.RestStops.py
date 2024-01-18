import sys
input = sys.stdin.readline

def solution(rf, rb, stops):
    stops.sort(key=lambda x:-x[1])
    answer = 0
    prev_stop = 0
    time = 0
    r = rf - rb
    for t, c in stops:
        if t < prev_stop:
            continue
        prev_stop = t
        answer += (t - time)*r*c
        time = t
    return answer

l, n, rf, rb = [int(x) for x in input().split(' ')]
stops = []
for i in range(n):
    stops.append([int(x) for x in input().split(' ')])

print(solution(rf, rb, stops))