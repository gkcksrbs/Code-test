# 너비 우선 탐색을 위한 deque import
from _collections import deque
import sys

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호 입력
n, m, k, s = map(int, sys.stdin.readline().split())
# 도시 그래프 생성
graph = [[] for _ in range(n+1)]
# 도시 그래프 정보 입력
for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
# 출발 도시부터의 거리 리스트 생성
distance = [-1 for _ in range(n+1)]
distance[s] = 0
# 너비 우선 탐색 실행
q = deque([s])

while q:
    val = q.popleft()

    for j in graph[val]:
        if distance[j] == -1: # 아직 방문하지 않은 도시인 경우
            # 최단 거리 입력
            distance[j] = distance[val] + 1
            q.append(j)
# distance 리스트에 입력 받은 거리 정보값이 없을 경우 -1 출력
if k not in distance:
    print(-1)
else:
    # distance 리스트에 입력 받은 거리 정보값이 있을 때 오름차순으로 출력
    for i in range(len(distance)):
        if distance[i] == k:
            print(i)
