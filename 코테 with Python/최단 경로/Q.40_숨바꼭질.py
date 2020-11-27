import heapq
# 무한대를 의미하는 값으로 10억을 설정
INF = int(1e9)
# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())
# 거리 리스트 무한대로 초기화 후 1번 노드는 0으로 초기화
distance = [INF]*(n+1)
distance[1] = 0
# 간선 정보 입력 리스트 초기화 및 입력
lst = [[] for _ in range(n+1)]

for _ in range(m):
    c1, c2 = map(int, input().split())
    lst[c1].append(c2)
    lst[c2].append(c1)
# 최단 거리가 가장 먼 노드 번호, 길이, 결과값 초기화
max_node = 0
max_distance = 0
result = []
# 다익스트라 알고리즘 사용을 위한 큐 초기화 (거리, 현재 노드번호)
q = [(0, 1)]
# 다익스트라 알고리즘 실행
while q:
    dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    if distance[now] < dist:
        continue
    # 현재 노드와 연결된 다른 노드 확인
    for i in lst[now]:
        cost = dist + 1
        # 현재 노드를 거쳐 가는 거리가 더 짧은 경우
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q, (cost, i))
# 가장 먼 노드, 거리, 결과 리스트 탐색
for i in range(1, n+1):
    if distance[i] > max_distance:
        max_node = i
        max_distance = distance[i]
        result = [max_node]

    elif max_distance == distance[i]:
        result.append(i)
# 결과값 출력
print(max_node, max_distance, len(result))
