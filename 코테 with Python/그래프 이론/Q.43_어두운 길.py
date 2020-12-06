import sys
# 입력을 빠르게 하기 위한 변수
input = sys.stdin.readline
# 집과 도로의 수 입력
n, m = map(int, input().split())
# 도로 정보 리스트
lst = []
# 도로 정보 입력
for _ in range(m):
    n1, n2, cost = map(int, input().split())
    lst.append((cost, n1, n2))
# 가로등 비용 순으로 정렬
lst.sort()
# 각 집 노드의 루트 노드 초기화
root = [0]*n

for i in range(n):
    root[i] = i


# 특정 원소의 집합을 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소의 집합을 합치는 함수
def union_parent(parent, node1, node2):
    node1 = find_parent(parent, node1)
    node2 = find_parent(parent, node2)
    if node1 < node2:
        root[node2] = node1
    else:
        root[node1] = node2


# 최소 비용 및 현재 가로등의 총 비용 초기화
result = 0
sum_cost = 0
# 최소 스패닝 트리 알고리즘 실행
for val, s, e in lst:
    sum_cost += val

    if find_parent(root, s) == find_parent(root, e):
        continue

    union_parent(root, s, e)
    result += val
# 결과값 출력
print(sum_cost - result)
