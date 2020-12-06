import sys
# 입력 빠르게 하기 위한 변수
input = sys.stdin.readline
# 탑승구의 수, 비행기의 수 입력
g, p = int(input()), int(input())
# 루트 노드 초기화
root = [0] * (g+1)

for i in range(g+1):
    root[i] = i


# 특정 원소가 속한 집합 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소의 집합을 합치는 함수
def union_parent(parent, n1, n2):
    n1 = find_parent(parent, n1)
    n2 = find_parent(parent, n2)

    if n1 < n2:
        parent[n2] = n1
    else:
        parent[n1] = n2


# 도킹할 수 있는 탑승구 정보 입력
data_lst = []

for _ in range(p):
    data_lst.append(int(input()))
# 결과값 초기화
count = 0
# 정보 탐색
for data in data_lst:
    if find_parent(root, data) == 0:
        break
    union_parent(root, find_parent(root, data), find_parent(root, data)-1)
    count += 1
# 결과값 출력
print(count)
