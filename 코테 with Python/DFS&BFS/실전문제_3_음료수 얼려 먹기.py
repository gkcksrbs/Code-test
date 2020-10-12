# 세로, 가로 입력
N, M = map(int, input().split())
# 구멍, 칸막이 입력
graph = []
for i in range(N):
    graph.append(list(input()))
# 아이스크림 개수
count = 0
# 아이스크림 개수 구하는 함수
def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if graph[x][y] == '0':
        graph[x][y] = '1'

        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)

        return True
    return False

for i in range(N):
    for j in range(M):
        if dfs(i, j):
            count += 1

print(count)


