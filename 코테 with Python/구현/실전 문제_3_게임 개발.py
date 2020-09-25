n, m = map(int, input().split())

d = [[0] * m for i in range(n)]
x, y, dir = map(int, input().split())
d[x][y] = 1

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

count = 1
turn_time = 0
while True:
    turn()
    nx = x + dx[dir]
    ny = y + dy[dir]

    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]

        if arr[nx][ny] == 0:
            x = nx
            y = ny

        else:
            break
        turn_time = 0

print(count)
