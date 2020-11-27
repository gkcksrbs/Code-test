from _collections import deque
# 무한대를 의미하는 값으로 10억으로 초기화
INF = int(1e9)
# 상,하,좌,우
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# 테스트케이스 수 입력
t = int(input())
# 테스트케이스 실행
for _ in range(t):
    # 화성 탐사 비용 그래프 리스트 초기화
    graph = []
    # 탐사 공간의 크기 입력
    n = int(input())
    # 화성 탐사 비용 입력
    for __ in range(n):
        graph.append(list(map(int, input().split())))
    # 너비 탐색 저장 리스트 초기화
    lst = [[INF] * n for _ in range(n)]
    lst[0][0] = graph[0][0]
    # 너비 우선 탐색 실행
    q = deque([(0, 0)])
    
    while q:
        x, y = q.popleft()
        # 상,하,좌,우 탐색
        for i in range(4):
            # 현재 좌표의 상,하,좌,우 다음 좌표
            nx, ny = x + dx[i], y + dy[i]
            # 다음 좌표가 그래프의 크기를 벗어나지 않을 경우 최소값 저장
            if 0 <= nx < n and 0 <= ny < n:
                if lst[nx][ny] > lst[x][y] + graph[nx][ny]:
                    lst[nx][ny] = lst[x][y] + graph[nx][ny]
                    q.append((nx, ny))
    # 결과값 출력
    print(lst[n-1][n-1])
