from itertools import combinations

n = int(input())
data = list(map(int, input().split()))
dp = [False] * (sum(data) + 1)
for i in range(1, len(data) + 1):
    for j in combinations(data, i):
        dp[sum(j)] = True
for i in range(1, len(dp)):
    if not dp[i]:
        print(i)
        break
