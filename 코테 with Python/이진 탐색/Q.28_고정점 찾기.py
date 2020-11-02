import sys
input = sys.stdin.readline
# 이진 탐색 함수
def binary_search(array, start, end):
    # 이진 탐색
    while start <= end:
        # 중간값
        mid = (start + end) // 2
        # 인덱스와 값이 동일하면 중간값 반환
        if array[mid] == mid:
            return mid
        # 인덱스의 값이 중간값보다 크다면
        elif array[mid] > mid:
            # 왼쪽 부분 탐색
            end = mid - 1
        # 인덱스의 값이 중간값보다 작다면
        else:
            # 오른쪽 부분 탐색
            start = mid + 1
    # 인덱스와 값이 동일한 값이 없을 경우 -1 반환
    return -1
# 원소의 개수 입력
n = int(input())
# 원소 리스트 입력
lst = list(map(int, input().split()))
# 이진 탐색 실행 후 결과값 출력
print(binary_search(lst, 0, n-1))
