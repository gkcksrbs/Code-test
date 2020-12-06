from _collections import deque
n = int(input())
present_lst = list(map(int, input().split()))
present_lst.sort()
q = deque(present_lst)
family = []
for i in range(3):
    family.append(q.popleft())
# while present_lst:
#     present = present_lst.pop(-1)
#     if family[1] >= family[2] + present:
#         family[2] += present
#     elif family[0] >= family[1] + present:
#         family[1] += present
#     else:
#         family[0] += present
while q:
    present = q.popleft()
    if family[1] >= family[0] + present:
        family[0] += present
    elif family[2] >= family[1] + present:
        family[1] += present
    else:
        family[2] += present
for i in family:
    print(i, end=' ')
