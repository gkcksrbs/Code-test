import sys
from bisect import bisect_left, bisect_right
# 입력 시간을 빠르게 하기 위한 변수
input = sys.stdin.readline
# left_val 이상 right_val 이하인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_val, right_val):
    right_index = bisect_right(array, right_val)
    left_index = bisect_left(array, left_val)
    return right_index - left_index
# 데이터의 개수, 찾고자 하는 값 입력
n, x = map(int, input().split())
# 데이터 리스트 입력
lst = list(map(int, input().split()))
# 찾고자 하는 값의 개수 계산
result = count_by_range(lst, x, x)
# x 가 존재하지 않으면 -1 출력
if result == 0:
    print(-1)
# x 가 존재하면 개수 출력
else:
    print(result)
