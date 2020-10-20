from _collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == -1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
n, m = map(int, input().split())
graph = []
for _ in range(n):
    tmp = list(map(int, input()))
    for i in range(len(tmp)):
        if tmp[i] == 1:
            tmp[i] = -1
    graph.append(tmp)
graph[0][0] = 1
bfs(0, 0)
print(graph[n-1][m-1])

