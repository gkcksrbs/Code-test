from _collections import deque
# 보드의 크기
size = int(input())
# 사과의 개수
apple_num = int(input())
# 보드에서 사과의 위치
apple_loc = [[False]*size for _ in range(size)]
for _ in range(apple_num):
    i, j = map(int, input().split())
    apple_loc[i-1][j-1] = True
# 뱀의 회전 횟수
turn_num = int(input())
# 뱀이 회전하는 시간과 회전 방향 리스트 저장
turn_lst = deque()
for _ in range(turn_num):
    turn_lst.append(list(map(str, input().split())))
for i in range(turn_num):
    turn_lst[i][0] = int(turn_lst[i][0])
# 뱀의 초기 상태 설정
snake_loc = [[False]*size for _ in range(size)]
snake_loc[0][0] = True
snake_lst = deque()
snake_head = [0, 0]
snake_lst.append(snake_head)
# 뱀의 방향
# [우, 하, 좌, 상]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
loc = 0

time = 0


def turn_right():
    global loc

    if loc == 3:
        loc = 0
    else:
        loc += 1

def turn_left():
    global loc

    if loc == 0:
        loc = 3
    else:
        loc -= 1

while True:
    time += 1

    nx = snake_lst[-1][0]
    ny = snake_lst[-1][1]

    nx += dx[loc]
    ny += dy[loc]

    if nx < 0 or ny < 0 or nx >= size or ny >= size:
        break
    if [nx, ny] in snake_lst:
        break

    snake_lst.append([nx, ny])
    snake_loc[nx][ny] = True

    if apple_loc[nx][ny]:
        apple_loc[nx][ny] = False
    else:
        tmp = snake_lst.popleft()
        snake_loc[tmp[0]][tmp[1]] = False

    if turn_lst.__len__() != 0:
        if turn_lst[0][0] == time:
            tmp1 = turn_lst.popleft()
            if tmp1[1] == 'D':
                turn_right()
            else:
                turn_left()

print(time)