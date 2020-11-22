# 무한을 의미하는 값으로 10억으 설정
INF = int(1e9)
# 노드의 개수 및 간선의 개수 입력
n, m = map(int, input().split())
# 2차원 리스트 생성 및 모든값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]
# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0
# 각 간선에 대한 정보를 입력 받고 그 값으로 초기화
for _ in range(m):
    # 각 두 노드 입력
    c1, c2 = map(int, input().split())
    # 두 노드간 이동 비용을 1로 설정
    graph[c1][c2] = 1
    graph[c2][c1] = 1
# 플로이드 워셜 알고리즘 실행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if k == i or k == j:
                continue
            if i == j:
                continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
# 거쳐 갈 노드 X 와 목적지 K 노드 입력
x, k = map(int, input().split())
# 결과값
distance = graph[1][k] + graph[k][x]
# 도달할 수 없는 경우 -1 출력
if distance >= INF:
    print(-1)
# 도달할 수 있는 경우 결과값 출력
else:
    print(distance)
