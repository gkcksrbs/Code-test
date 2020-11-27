# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)
# 학생 수, 두 학생 성적을 비교한 결과 수 입력
n, m = map(int, input().split())
# 플로이드 워셜 알고리즘 사용을 위한 리스트 무한대 값으로 초기화
lst = [[INF]*(n+1) for _ in range(n+1)]
# 결과값 변수 초기화
result = 0
# 같은 학생의 최단 거리를 0으로 설정
for i in range(1, n+1):
    lst[i][i] = 0
# 두 학생의 성적 비교 결과 입력
for _ in range(m):
    loser, winner = map(int, input().split())
    lst[loser][winner] = 1
# 플로이드 워셜 알고리즘 실행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            lst[i][j] = min(lst[i][j], lst[i][k] + lst[k][j])
# 각 학생에 따라 한명씩 확인하며 도달 가능한지 체크
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if lst[i][j] != INF or lst[j][i] != INF:
            count += 1
    if count == n:
        result += 1
# 결과값 출력
print(result)