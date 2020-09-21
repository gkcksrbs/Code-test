import sys

N = int(sys.stdin.readline())
money = [500, 100, 50, 10]
count = 0

for i in money:
    count += N // i
    N %= i

print(count)


# min_count = 1e9
# def DFS(charge, count):
#     global min_count
#     if charge == 0:
#         if count < min_count:
#             min_count = count
#     if charge < 500:
#         count += charge // 500
#         DFS(charge % 500, count)
#
#     if charge < 100:
#         count += charge // 100
#         DFS(charge % 100, count)
#
#     if charge < 50:
#         count += charge // 50
#         DFS(charge % 50, count)
#
#     if charge < 10:
#         count += charge // 10
#         DFS(charge % 10, count)
# DFS(1260, 0)
# print(min_count)
