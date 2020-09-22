import sys

N, M = map(int, sys.stdin.readline().split())
card_lst = []
tmp = []

for i in range(N):
    card_lst.append(list(map(int, sys.stdin.readline().split())))
    tmp.append(min(card_lst[i]))

print(max(tmp))