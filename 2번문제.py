import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []

for i in range(n, m+1):
    data = list(str(i))
    tmp = 1

    for j in data:
        tmp *= int(j)

    result.append(tmp)

print(sum(result))