# 화폐의 개수, m 원 입력
n, m = map(int, input().split())
# 화폐의 가치를 저장할 리스트 생성
lst = []
# 화폐 단위 입력
for _ in range(n):
    lst.append(int(input()))
# DP 테이블 생성
d = [10001]*10001
d[0] = 0
# 다이나믹 프로그래밍 진행(보텀업)
for i in range(n):
    for j in range(lst[i], m+1):
        if d[j - lst[i]] != 10001:
            d[j] = min(d[j], d[j - lst[i]] + 1)
# 해당 화폐로 m 원을 만들 수 없을 경우 -1 출력
if d[m] == 10001:
    print(-1)
# 해당 화폐로 m 원을 만들 수 있을 경우 결과값 출력
else:
    print(d[m])
