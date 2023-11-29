import sys
from itertools import combinations

input = sys.stdin.readline

dwarf = []

for _ in range(9):
    dwarf.append(int(input()))

cases = combinations(dwarf, 7)
for c in cases:
    if sum(c) == 100:
        for item in sorted(c):
            print(item)
        break