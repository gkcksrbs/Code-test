import sys
# 입력 시간 빠르게 하기 위한 변수
input = sys.stdin.readline
# 이진 탐색 함수
def binary_search(array, x, start, end):
    # 이진 탐색
    while start <= end:
        # 중간 점
        mid = (start + end) // 2
        # 찾는 부품이 매장에 존재하면 True 반환
        if array[mid] == x:
            return True
        # 중간점의 값보다 찾는 값이 더 작을 때
        elif array[mid] > x:
            # 왼쪽 부분 탐색
            end = mid - 1
        # 중간점의 값보다 찾는 값이 더 클때
        else:
            # 오른쪽 부분 탐색
            start = mid + 1
    return False
# 가게 부품 개수 입력
n = int(input())
# 가게 부품 입력 후 정렬
lst = sorted(list(map(int, input().split())))
# 찾는 부품 개수 입력
m = int(input())
# 찾는 부품 입력
find_lst = list(map(int, input().split()))
# 찾는 부품 하나씩 확인
for i in find_lst:
    # 부품이 존재하는지 확인
    result = binary_search(lst, i, 0, n-1)
    # 부품이 있을 경우
    if result:
        print('yes', end=' ')
    # 부품이 없을 경우
    else:
        print('no', end=' ')
