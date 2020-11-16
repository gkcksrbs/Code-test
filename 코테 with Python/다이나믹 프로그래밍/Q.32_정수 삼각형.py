# 위층 좌,우 좌표
dx, dy = [-1, -1], [-1, 0]
# 삼각형의 크기 입력
n = int(input())
# 그래프 리스트
lst = []
# 결과 리스트
result = []
# 그래프 입력
for i in range(n):
    lst.append(list(map(int, input().split())))
# DP 테이블 초기화
d = []

for i in range(n):
    tmp = [-1]*(i+1)
    d.append(tmp)
    
d[0][0] = lst[0][0]
# 다이나믹 프로그래밍 실행
for i in range(1, n):
    for j in range(len(d[i])):
        # 위층의 좌우 인덱스 입력하는 리스트
        tmp = [0]
        # 위층의 좌우 두번 탐색
        for k in range(2):
            # 위층의 좌표
            px, py = i + dx[k], j + dy[k]
            # 해당 좌표가 그래프의 범위를 벗어나지 않았을 경우
            if 0 <= py < len(d[i-1]):
                # 해당 좌표 추가
                tmp.append(d[px][py])
        # DP 테이블에 최대값과 합산
        d[i][j] = lst[i][j] + max(tmp)
        # 1층일 경우 결과 리스트에 DP 테이블 해당 좌표에 있는 값 추가
        if i == n-1:
            result.append(d[i][j])
# 결과값 출력
print(max(result))