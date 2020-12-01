import sys
# 입력을 빠르게 하기 위한 변수
input = sys.stdin.readline
# 학생 수, 연산의 개수 입력
n, m = map(int, input().split())
# 부모 테이블 초기화
parent_lst = [0] * (n+1)

for i in range(n+1):
    parent_lst[i] = i


# 특정 원소가 속한 집합 찾는 함수
def find_parent(parent, x):
    # 루트 노드가 아닐 경우
    if parent[x] != x:
        # 루트 노드 찾을 때까지 함수 재귀적 호출
        parent[x] = find_parent(parent, parent[x])
    # 루트 노드 반환
    return parent[x]


# 두 원소가 속한 집합 합치는 함수
def union_parent(parent, n1, n2):
    # 두 원소의 루트 노드 찾기 위한 함수 실행
    n1 = find_parent(parent, n1)
    n2 = find_parent(parent, n2)
    # 작은 번호의 루트 노드로 저장
    if n1 < n2:
        parent[n2] = n1
    else:
        parent[n1] = n2


# 각 연산 입력 및 수행
for _ in range(m):
    # 연산, 두 원소 입력
    op, a, b = map(int, input().split())
    # 팀 합치는 연산일 경우 팀 합치기
    if op == 0:
        union_parent(parent_lst, a, b)
    # 같은 팀 여부 확인 연산일 경우
    else:
        # 두 원소의 루트 노드 확인
        pa = find_parent(parent_lst, a)
        pb = find_parent(parent_lst, b)
        # 두 원소의 루트 노드가 같을 경우 YES 출력
        if pa == pb:
            print('YES')
        # 두 원소의 루트 노드가 다를 경우 NO 출력
        else:
            print('NO')
