# 다시 풀어보기 주석 pass
from itertools import combinations

n = int(input())
graph, teacher, empty = [], [], []
result = False

for i in range(n):
    data = list(map(str, input().split()))

    for j in range(len(data)):
        if data[j] == 'T':
            teacher.append((i, j))

        elif data[j] == 'X':
            empty.append((i, j))

    graph.append(data)

def process():

    for x, y in teacher:
        for direction in range(4):
            if dfs(x, y, direction):
                return True
    return False

def dfs(x, y, direction):

    if direction == 0:
        while x >= 0:
            if graph[x][y] == 'S':
                return True
            if graph[x][y] == 'O':
                return False
            x -= 1

    if direction == 1:
        while x < n:
            if graph[x][y] == 'S':
                return True
            if graph[x][y] == 'O':
                return False
            x += 1

    if direction == 2:
        while y >= 0:
            if graph[x][y] == 'S':
                return True
            if graph[x][y] == 'O':
                return False
            y -= 1

    if direction == 3:
        while y < n:
            if graph[x][y] == 'S':
                return True
            if graph[x][y] == 'O':
                return False
            y += 1

    return False

for i in combinations(empty, 3):

    for x, y in i:
        graph[x][y] = 'O'

    if not process():
        result = True
        break

    for x, y in i:
        graph[x][y] = 'X'

if result:
    print('YES')
else:
    print('NO')
