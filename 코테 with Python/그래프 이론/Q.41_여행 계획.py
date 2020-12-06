import sys
# 입력 빠르게 하기 위한 변수
input = sys.stdin.readline
# 여행지 수, 여행 계획에 속한 도시 수 입력
n, m = map(int, input().split())
# 연결 정보 저장 리스트
lst = []
# 여행지 연결 정보 입력
for i in range(n):
    data = list(map(int, input().split()))

    for j in range(i):
        if data[j] == 1:
            lst.append((i+1, j+1))
# 부모 노드 초기화
root = [0] * (n+1)

for i in range(n+1):
    root[i] = i


# 특정 원소가 속한 집합 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소의 집합 합치는 함수
def union_parent(parent, n1, n2):
    root_n1 = find_parent(parent, n1)
    root_n2 = find_parent(parent, n2)
    if root_n1 < root_n2:
        parent[root_n2] = root_n1
    else:
        parent[root_n1] = root_n2


# 연결 정보 집합 합치기
for i, j in lst:
    union_parent(root, i, j)
# 여행 계획 도시 입력
result = list(set((map(int, input().split()))))
# 같은 집합인지 판별하는 bool 변수
is_union = True
# 같은 집합에 속했는지 판별
for i in range(len(result)-1):
    if find_parent(root, result[i]) != find_parent(root, result[i+1]):
        is_union = False
        break
    else:
        continue
# 결과값 출력
if is_union:
    print('YES')
else:
    print('NO')
