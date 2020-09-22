import sys

# N, K = map(int, sys.stdin.readline().split())
#
# count = 0
#
# while True:
#     if N == 1:
#         break
#     if N % K == 0:
#         N //= K
#         count += 1
#     else:
#         N -= 1
#         count += 1
#
# print(count)

N, K = map(int, sys.stdin.readline().split())

count = 0

while True:

    tmp = (N // K) * K
    count += (N - tmp)
    N = tmp

    if N < K:
        count += (N - 1)
        break

    N //= K
    count += 1

print(count)