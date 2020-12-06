from _collections import deque
import sys
dx, dy = [0, 1], [1, 0]
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

if n == 1:
    print(graph[n-1][n-1])

else:
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = graph[0][0]

    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        for i in range(2):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if dp[nx][ny] < dp[x][y] + graph[nx][ny]:
                    dp[nx][ny] = dp[x][y] + graph[nx][ny]
                    q.append((nx, ny))

    print(dp[n-1][n-1])
