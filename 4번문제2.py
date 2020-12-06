n = int(input())
ans = int(1e9)
present_lst = list(map(int, input().split()))
w = sum(present_lst)
dp = [[[False]*668 for _ in range(668)] for _ in range(21)]
first = second = third = 0
dp[0][0][0] = True
for i in range(1, n+1):
    for j in range(668):
        for k in range(668):
            if j - present_lst[i] < 0:
                tmp1 = False
            else:
                tmp1 = dp[i-1][j-present_lst[i]][k]
            if k - present_lst[i] < 0:
                tmp2 = False
            else:
                tmp2 = dp[i-1][j][k-present_lst[i]]
            dp[i][j][k] = (dp[i-1][j][k] or tmp1 or tmp2)
for i in range(668):
    for j in range(668):
        if dp[n][i][j]:
            if w - (i+j) > i and i >= j and w - (i+j) - j <= ans:
                ans = w - (i+j) - i
                first = w - (i+j)
                second = i
                third = j
print(first, second, third)
