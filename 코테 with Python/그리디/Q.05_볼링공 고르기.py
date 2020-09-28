from itertools import combinations

N, M = map(int, input().split())
weight = list(map(int, input().split()))
lst = []

for i in combinations(weight, 2):
    if i[0] != i[1]:
        lst.append(i)

print(len(lst))