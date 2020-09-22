import sys

N = int(sys.stdin.readline())
x, y = 1, 1
lst = list(map(str, sys.stdin.readline().split()))
move = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in lst:
    index = move.index(i)
    nx = x + dx[index]
    ny = y + dy[index]

    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue

    x = nx
    y = ny

print(x, y)