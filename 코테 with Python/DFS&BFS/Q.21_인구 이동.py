import sys
from _collections import deque

input = sys.stdin.readline
# 상,하,좌,우
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# 그래프의 크기, 인구 차이 범위 입력
n, l, r = map(int, input().split())
# 그래프 생성
graph = []
# 그래프 입력
for _ in range(n):
    graph.append(list(map(int, input().split())))
# 인구 이동 실행 함수
def go():
    # 인구 이동 발생 횟수
    result = 0
    # 모든 나라에 연합이 없을 때까지
    while not equal():
        # 연합 묶음 리스트
        guild = [[0]*n for _ in range(n)]
        # 각 연합 구별 단위
        num = 1
        # 그래프 안의 모든 나라 탐색
        for i in range(n):
            for j in range(n):
                # 아직 연합이 정해지지 않았을 때
                if guild[i][j] == 0:
                    # 너비 우선 탐색 실행
                    bfs(i, j, guild, num)
                    # 다음 연합 그룹
                    num += 1
        # 인구 이동 횟수 증가
        result += 1
    # 인구 이동 횟수 결과 출력
    print(result)
# 주변 나라와의 인구 차이수가 l 과 r 사이에 있는지 아닌지 판별하는 함수
def equal():
    # 모든 나라 탐색
    for i in range(n):
        for j in range(n):
            # 나라별 상,하,좌,우 탐색
            for k in range(4):
                # 현재 나라의 인접 나라의 좌표
                nx, ny = i + dx[k], j + dy[k]
                # 다음 나라의 좌표가 그래프의 범위를 벗어나지 않을 경우
                if 0 <= nx < n and 0 <= ny < n:
                    # 두 나라의 차이가 l 과 r 사이에 있을 때 false 반환
                    if l <= abs(graph[i][j] - graph[nx][ny]) <= r:
                        return False
    # 모든 나라가 연합이 만들어지지 않을 때 true 반환
    return True
# 너비 우선 탐색
def bfs(x, y, lst, num):
    # bfs 탐색을 위한 queue 생성
    q = deque()
    # 너비 탐색을 시작하는 좌표 queue 삽입
    q.append((x, y))
    # 연합의 총 인구수 저장 변수
    total = 0
    # 연합 총 나라 수 저장 변수
    count = 0
    # q가 빌 때까지
    while q:

        px, py = q.popleft()
        # 해당 나라의 연합 번호 저장
        lst[px][py] = num
        # 해당 나라의 인구 수 더하기
        total += graph[px][py]
        # 연합에 나라 수 더하기
        count += 1
        # 상,하,좌,우 탐색
        for i in range(4):
            # 다음 좌표
            nx = px + dx[i]
            ny = py + dy[i]
            # 다음 좌표가 그래프의 범위 안에 있을 경우
            if 0 <= nx < n and 0 <= ny < n:
                # 다음 나라와 현재 나라의 인구 수 차이가 l 과 r 사이에 있을 경우
                if l <= abs(graph[px][py] - graph[nx][ny]) <= r:
                    # 다음 나라가 연합이 없을 때
                    if lst[nx][ny] == 0:
                        # 연합에 추가
                        lst[nx][ny] = num
                        # 다음 나라의 너비 탐색을 위한 다음 나라 좌표 queue 에 삽입
                        q.append((nx, ny))
    # 해당 연합이 2개 이상의 나라를 가지고 있을 때
    if count > 1:
        # 모든 좌표 탐색
        for i in range(n):
            for j in range(n):
                # 해당 연합일 때
                if lst[i][j] == num:
                    # 인구 이동
                    graph[i][j] = total // count
# 인구 이동 실행
go()
