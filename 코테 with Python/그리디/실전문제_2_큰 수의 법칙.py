import sys

N, M, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
sum = 0
count = 0
tmp = 0

lst.sort()

while tmp != M:
    if count == K:
        sum += lst[len(lst)-2]
        count = 0
    else:
        sum += max(lst)
        count += 1
    tmp += 1

print(sum)

