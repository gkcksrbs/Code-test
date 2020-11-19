"""
이진 탐색 파트에서
https://github.com/gkcksrbs/Code-test/blob/master/%EC%9D%B4%EB%B6%84%20%ED%83%90%EC%83%89/Baekjoon_12015_%EA%B0%80%EC%9E%A5%20%EA%B8%B4%20%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4%202.py
"Baekjoon_12015_가장 긴 증가하는 부분 수열" 문제와 비슷한 문제
"""
from bisect import bisect_left
# 병사의 수 입력
n = int(input())
# 병사의 전투력 입력
lst = list(map(int, input().split()))
# LIS 사용을 위한 배열 뒤집기
lst.reverse()
# DP 테이블 초기화
d = [0]
# 다이나믹 프로그래밍 실행(보텀업)
for i in range(len(lst)):
    # DP 테이블의 마지막 인덱스의 값이 리스트의 값보다 작다면
    if d[-1] < lst[i]:
        # DP 테이블에 해당 리스트 값 추가
        d.append(lst[i])
    # DP 테이블의 마지막 인덱스의 값이 리스트의 값보다 크거나 같다면
    else:
        # DP 테이블에서 해당 리스트의 값이 들어갈 수 있는 인덱스 값 탐색
        index = bisect_left(d, lst[i])
        # DP 테이블에 해당 인덱스에 리스트 값 입력
        d[index] = lst[i]
# 결과값 출력
print(n-len(d)+1)