"""
백준이 퇴사하기 전까지 주어진 상담 일정표 중 최대 수익을 구하는 프로그램

1. n일이 주어졌을 때 i = (n-1, n-2, n-3, ... ,1)로 두면 i 일부터 n 일까지 일했을 때 최대 수익을 DP 테이블에 저장
2. i = 1까지 탐색 후 DP 테이블 내의 최대 값 출력
"""
# 퇴사하기 까지 남은 일 수 입력
n = int(input())
# 상담 일정표 리스트 t = 해당 상담이 걸리는 시간, v = 해당 상담의 금액
t = []
v = []
# DP 테이블 초기화
d = [0] * (n+1)
# 결과값
max_val = 0
# 상담 일정표 입력
for _ in range(n):
    time, val = map(int, input().split())
    t.append(time)
    v.append(val)
# 다이나믹 프로그래밍 실행(탑다운)
for i in range(n-1, -1, -1):
    # 해당 상담이 끝나는 날짜
    time = t[i] + i
    # 상담이 끝나는 날짜가 퇴사 날짜와 같거나 전이라면
    if time <= n:
        # DP 테이블에 최대 수익 입력
        d[i] = max(v[i] + d[time], max_val)
        max_val = d[i]
    # 상담이 끝나는 날짜가 퇴사 날짜를 지나게 되면
    else:
        # DP 테이블에 최대 수익 입력
        d[i] = max_val
# 결과값 출력
print(max_val)