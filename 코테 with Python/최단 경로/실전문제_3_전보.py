import sys
import heapq
# 입력을 빠르게 하기 위한 변수
input = sys.stdin.readline
# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)
# 노드의 개수, 간선의 개수, 시작 노드 입력
n, m, c = map(int, input().split())
# 각 노드의 정보를 담는 리스트 생성
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (n+1)
# 모든 간선 정보 입력 받기
for _ in range(m):
    # 시작점, 끝점, 비용 입력
    s, e, v = map(int, input().split())
    # 그래프에 추가
    graph[s].append((e, v))
# 다익스트라 알고리즘 함수
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로 0으로 설정후 큐에 삽입
    heapq.heappush(q, (0, c))
    distance[c] = 0
    # 큐가 빌때까지
    while q:
        # 가장 최단거리가 짦은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 해당 위치의 거리가 큐에 꺼낸 거리보다 작다면 해당 루프 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
# 다익스트라 알고리즘 실행
dijkstra(c)
# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중 가장 멀리 있는 노드의 최단거리
max_distance = 0

for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)
# 결과값 출력
print(count - 1, max_distance)