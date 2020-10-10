from itertools import combinations

N, M = map(int, input().split())
city = []
house = []
chicken = []
comb = []

for _ in range(N):
    city.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

for i in combinations(chicken, M):
    comb.append(i)

tmp2 = []
for i in range(len(comb)):
    tmp1 = []
    for j in range(len(house)):
        tmp = []
        for k in range(len(comb[i])):
            dist = abs(house[j][0] - comb[i][k][0]) + abs(house[j][1] - comb[i][k][1])
            tmp.append(dist)
        tmp1.append(min(tmp))
    tmp2.append(sum(tmp1))

print(min(tmp2))
