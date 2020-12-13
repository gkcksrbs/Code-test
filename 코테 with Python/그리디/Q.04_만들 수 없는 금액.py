# 비효율
# from itertools import combinations
#
# N = int(input())
# coin = list(map(int, input().split()))
# lst = []
#
# for i in range(1, N+1):
#     for j in combinations(coin, i):
#         lst.append(sum(j))
#
# lst = list(set(lst))
# last = lst[len(lst)-1]
# Min = 0
#
# for i in range(1, last+1):
#     if i not in lst:
#         Min = i
#
# if min == 0:
#     print(last+1)
# else:
#     print(Min)

import sys
# 입력 빠르게 하기 위한 변수
input = sys.stdin.readline
# 동전의 개수 입력
n = int(input())
# 각 동전의 화폐 단위 입력
data = list(map(int, input().split()))
# 결과값
target = 1
# 모든 동전 탐색
for x in data:
    if target < x:
        break
    target += x
# 결과값 출력
print(target)
