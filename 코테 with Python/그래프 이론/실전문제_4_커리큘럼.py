# 다시 풀기
import sys
from _collections import deque
import copy
n = int(input())
in_degree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)
for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        in_degree[i] += 1
        graph[x].append(i)


def topology_sort():
    q = deque()
    result = copy.deepcopy(time)

    for j in range(1, n+1):
        if in_degree[j] == 0:
            q.append(j)

    while q:
        now = q.popleft()
        for j in graph[now]:
            result[j] = max(result[j], result[now] + time[j])
            in_degree[j] -= 1
            if in_degree[j] == 0:
                q.append(j)

    for j in range(1, n+1):
        print(result[j])

topology_sort()
