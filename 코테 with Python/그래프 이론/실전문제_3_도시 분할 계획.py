import sys
# 입력을 빠르게 하기 위한 변수
input = sys.stdin.readline
# 집의 개수, 도로의 개수 입력
n, m = map(int, input().split())
# 부모 노드 리스트 초기화
parent_lst = [0] * (n+1)
for i in range(n+1):
    parent_lst[i] = i


# 특정 원소가 속한 집합 찾는 함수
def find_parent(parent, x):
    # 자기 자신이 루트 노드가 아닐 경우
    if parent[x] != x:
        # 루트 노드 찾도록 재귀적으로 함수 호출
        parent[x] = find_parent(parent, parent[x])
    # 루트 노드 반환
    return parent[x]


# 두 원소 속한 집합 합치는 함수
def union_parent(parent, n1, n2):
    # 두 원소의 루트 노트 찾기
    n1 = find_parent(parent, n1)
    n2 = find_parent(parent, n2)
    # 두 루트 노드 중 작은 번호로 루트 노드 설정
    if n1 < n2:
        parent[n2] = n1
    else:
        parent[n1] = n2


# 도로 정보 리스트 초기화
lst = []
# 도로 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    lst.append([c, a, b])
# 도로 유지비 별로 정렬
lst.sort()
# 결과값 초기화
result = 0
# 최소 신장 트리에 포함 된 도로 중 비용이 큰 도로 초기화
last = 0
# 도로 정보 탐색
for cost, e1, e2 in lst:
    # 두 마을이 같은 집합에 속하지 않을 경우
    if find_parent(parent_lst, e1) != find_parent(parent_lst, e2):
        # 마을의 집합 합치기
        union_parent(parent_lst, e1, e2)
        # 결과값에 유지비 더하기
        result += cost
        # 비용이 큰 도로 설정
        last = cost
# 결과값 출력
print(result-last)
