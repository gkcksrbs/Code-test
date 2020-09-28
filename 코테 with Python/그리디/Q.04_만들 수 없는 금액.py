from itertools import combinations

N = int(input())
coin = list(map(int, input().split()))
lst = []

for i in range(1, N+1):
    for j in combinations(coin, i):
        lst.append(sum(j))

lst = list(set(lst))
last = lst[len(lst)-1]
Min = 0

for i in range(1, last+1):
    if i not in lst:
        Min = i

if min == 0:
    print(last+1)
else:
    print(Min)