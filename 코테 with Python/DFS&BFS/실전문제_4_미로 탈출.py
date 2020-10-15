from _collections import deque
# 가로, 세로 입력
n, m = map(int, input().split())
# 미로 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        count = 2
        px, py = q.popleft()

        for j in range(4):
            nx = px + dx[j]
            ny = py + dy[j]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] += graph[px][py]
                q.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0, 0))