import sys
from _collections import deque
# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 그래프의 크기, 바이러스 종류의 개수 입력
n, k = map(int, sys.stdin.readline().split())
# 그래프 입력
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
# 바이러스 위치, 시간, 좌표 입력을 위한 리스트 생성
loc_lst = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            loc_lst.append((graph[i][j], 0, i, j))
# s 초 뒤에 좌표(x, y) 대한 정보 입력
s, x, y = map(int, sys.stdin.readline().split())
# 번호가 낮은 바이러스부터 증식하기 위한 리스트 정렬
loc_lst.sort()
# BFS 적용을 위한 queue 생성
q = deque(loc_lst)
# queue 가 빌 때까지 탐색
while q:
    virus, time, px, py = q.popleft()
    # 입력된 시간을 초과하였을 경우 while 루프 벗어남
    if time >= s:
        break
    # 상,하,좌,우 탐색
    for j in range(4):
        nx = px + dx[j]
        ny = py + dy[j]
        # 다음 좌표가 그래프의 크기를 벗어날 경우 pass
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        # 다음 좌표가 0일 경우 바이러스 침투
        if graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append((virus, time+1, nx, ny))
# 해당 좌표의 바이러스 종류 출력
print(graph[x-1][y-1])