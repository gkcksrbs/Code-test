# a = 97

import sys

data = sys.stdin.readline()

x = int(data[1])
y = ord(data[0]) - 96

dxdy = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2),(-1,-2)]
lst = []

for i in dxdy:
    nx = x + i[0]
    ny = y + i[1]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue

    lst.append((nx, ny))

print(len(lst))