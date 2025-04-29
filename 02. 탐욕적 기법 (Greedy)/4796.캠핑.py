import sys
input = sys.stdin.readline

L, P, V = list(map(int, input().strip().split(' ')))
idx = 0

while L != 0:
    idx += 1
    ans = (V//P)*L + min((V%P),L)
    print(f"Case {idx}: {ans}")
    L, P, V = list(map(int, input().split(' ')))
