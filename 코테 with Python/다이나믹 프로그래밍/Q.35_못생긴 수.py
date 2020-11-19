from _collections import deque
# n 번쨰 못생긴 수를 출력하기 위한 n 입력
n = int(input())
# DP 테이블 초기화
d = [1]
# Queue 스택 생성
tmp = deque([1])
# 프로그래밍 실행
while True:
    # DP 테이블이 입력 범위를 넘어가게 되면 break
    if len(d) >= n*2:
        break
    q = tmp.popleft()
    val1, val2, val3 = q*2, q*3, q*5
    if val1 not in d:
        d.append(val1)
        tmp.append(val1)
    if val2 not in d:
        d.append(val2)
        tmp.append(val2)
    if val3 not in d:
        d.append(val3)
        tmp.append(val3)
# DP 테이블 정렬
d.sort()
# 결과값 출력
print(d[n-1])
