import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()


def solution():
    for i in combinations(lst, 3):
        if i[0] < i[1] < i[2]:
            return 'YES'
    return 'NO'


if n < 3:
    print('NO')
else:
    print(solution())
