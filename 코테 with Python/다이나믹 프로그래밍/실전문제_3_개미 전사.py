# 식량창고의 개수 입력
n = int(input())
# 각 식량창고에 저장된 식량의 개수 입력
lst = list(map(int, input().split()))
# DP 테이블 초기화
d = [0] * 100
# 다이나믹 프로그래밍 진행
d[0] = lst[0]
d[1] = max(lst[0], lst[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + lst[i])
# 결과값 출력
print(d[n-1])