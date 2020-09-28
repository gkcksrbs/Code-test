N = int(input())
scared_lst = list(map(int, input().split()))
scared_lst.sort()

count = 0
group = 0

for i in scared_lst:
    count += 1
    if count >= i:
        group += 1
        count = 0

print(group)