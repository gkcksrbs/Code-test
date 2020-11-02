import sys
# 입력 시간 빠르게 하기 위한 input 변수
input = sys.stdin.readline
# 떡의 개수, 요청한 떡의 길이 입력
n, m = map(int, input().split())
# 떡의 개별 높이 리스트 입력
lst = list(map(int, input().split()))
# 시작점, 끝점 초기화
start = 0
end = max(lst)
# 이진 탐색 결과값 초기화
result = 0
# 이진 탐색 실행
while start <= end:
    # 떡의 총 길이
    total = 0
    # 중간값
    mid = (start + end) // 2

    for i in lst:
        # 자르고 남은 떡의 길이가 양수 일때
        if i - mid > 0:
            # 떡의 총 길이에 합산
            total += i - mid
    # 떡의 총 길이가 요청한 떡의 길이보다 작을 경우
    if total < m:
        # 왼쪽 부분 탐색
        end = mid - 1
    # 떡의 총 길이가 요청한 떡의 길이보다 크거나 같을 경우
    else:
        result = mid
        # 오른쪽 부분 탐색
        start = mid + 1
# 결과 출력
print(result)
