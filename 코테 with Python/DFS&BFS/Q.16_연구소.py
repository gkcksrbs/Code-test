import sys
from itertools import combinations
# 깊이 우선 탐색
def dfs(x, y):
    # 바이러스 침투
    tmp[x][y] = 2
    # 상,하,좌,우 4방향으로 바이러스 전염
    for num in range(4):
        nx = x + dx[num]
        ny = y + dy[num]
        # 다음 좌표가 그래프의 크기를 벗어날 경우 pass
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        # 다음 좌표가 빈칸일 경우
        if tmp[nx][ny] == 0:
            dfs(nx, ny)
# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 그래프의 크기 입력
n, m = map(int, sys.stdin.readline().split())
# 그래프 입력
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
# 조합 사용을 위한 리스트
lst = []
for i in range(n*m):
    lst.append(i)
# 바이러스가 퍼지지 않은 빈칸 개수 저장을 위한 리스트
result = []
# 3개의 벽을 설치할 수 있는 조합
for i in combinations(lst, 3):
    # 그래프의 임시 그래프
    tmp = []
    # 그래프 복사
    for j in range(len(graph)):
        tmp.append(graph[j].copy())  # tmp = graph.copy() 를 사용하였더니 리스트가 공유됨
    # 벽으로 세울 3개의 리스트 좌표 
    x0 = i[0] // m
    y0 = i[0] % m
    
    x1 = i[1] // m
    y1 = i[1] % m
    
    x2 = i[2] // m
    y2 = i[2] % m
    # 3개의 좌표가 모두 0일 경우
    if tmp[x0][y0] == 0 and tmp[x1][y1] == 0 and tmp[x2][y2] == 0:
        # 3개의 좌표를 벽 생성
        tmp[x0][y0] = tmp[x1][y1] = tmp[x2][y2] = 1
        # 바이러스 전파
        for j in range(n):
            for k in range(m):
                if tmp[j][k] == 2:
                    dfs(j, k)
        # 바이러스가 전염되지 않은 빈칸의 개수
        count = 0
        for j in range(n):
            for k in range(m):
                if tmp[j][k] == 0:
                    count += 1
        # 빈칸의 개수를 리스트에 저장
        result.append(count)
# 빈칸 영역의 최대값 출력
print(max(result))
