import sys
# 깊이 우선 탐색
def dfs(index, num):
    global add, sub, mul, div, max_val, min_val
    # 모든 계산이 완료되었을 때 최댓값, 최솟값 저장
    if index == n:
        max_val = max(max_val, num)
        min_val = min(min_val, num)
    else:
        # 더하기 연산이 존재할 때
        if add > 0:
            add -= 1
            dfs(index+1, num + a[index])
            add += 1
        # 빼기 연산이 존재할 때
        if sub > 0:
            sub -= 1
            dfs(index+1, num - a[index])
            sub += 1
        # 곱하기 연산이 존재할 때
        if mul > 0:
            mul -= 1
            dfs(index+1, num * a[index])
            mul += 1
        # 나누기 연산이 존재할 때
        if div > 0:
            div -= 1
            dfs(index+1, int(num / a[index])) # 음수 상황일 때를 대비하기 위함
            div += 1
# 수의 개수 입력
n = int(sys.stdin.readline())
# 수 입력
a = list(map(int, sys.stdin.readline().split()))
# 연산 개수 입력
add, sub, mul, div = map(int, sys.stdin.readline().split())
# 최댓값, 최솟값 초기화
max_val = -1e9
min_val = 1e9
# 연산자 끼워 넣기 수행
dfs(1, a[0])
# 최댓값, 최솟값 출력
print(max_val)
print(min_val)