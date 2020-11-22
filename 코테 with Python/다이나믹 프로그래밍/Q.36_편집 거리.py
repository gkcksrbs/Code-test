# 다시 풀어볼 문제
a = list(input())
b = list(input())
lenA = len(a)
lenB = len(b)
dp = [[0]*(lenB + 1) for _ in range(lenA+1)]
for i in range(1, lenB+1):
    dp[0][i] = i
for i in range(1, lenA+1):
    dp[i][0] = i
for i in range(1, lenA+1):
    for j in range(1, lenB+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
print(dp[lenA-1][lenB-1])