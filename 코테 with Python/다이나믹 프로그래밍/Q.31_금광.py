# 테스트 케이스 수 입력
t = int(input())
# 왼쪽 위, 왼쪽, 왼쪽 아래
dx, dy = [-1, 0, 1], [-1, -1, -1]
# 테스트 케이스 실행
for _ in range(t):
    # 행, 열 입력
    n, m = map(int, input().split())
    # 각 칸의 금의 크기 입력
    lst = list(map(int, input().split()))
    # 그래프 생성
    graph = [[0]*m for _ in range(n)]
    # m 번째 열에 해당하는 DP 테이블의 값을 저장하는 리스트
    result = []
    # 그래프 입력
    for i in range(len(lst)):
        row = i // m
        col = i % m
        graph[row][col] = lst[i]
    # DP 테이블 초기화
    d = [[-1]*m for _ in range(n)]

    for i in range(len(graph)):
        d[i][0] = graph[i][0]
    # 다이나믹 프로그래밍 실행
    for i in range(m):
        for j in range(n):
            # 왼쪽 그래프의 금의 크기 저장하는 리스트
            tmp = [0]
            # 왼쪽 위, 왼쪽, 왼쪽 아래 탐색
            for k in range(3):
                # 왼쪽 위, 왼쪽, 왼쪽 아래 좌표
                nx, ny = j + dx[k], i + dy[k]
                # 해당 좌표가 그래프 범위 안에 존재할 경우
                if 0 <= nx < n and 0 <= ny < m:
                    tmp.append(d[nx][ny])
            # DP 테이블에 최대값 저장
            d[j][i] = graph[j][i] + max(tmp)
            # DP 테이블 탐색 중 해당 인덱스가 마지막 열이면
            if i == m-1:
                # 결과값 리스트에 DP 테이블 해당 인덱스 값 추가
                result.append(d[j][i])
    # 결과값 출력
    print(max(result))