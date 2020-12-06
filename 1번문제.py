# data = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
# user_input = int(input())
# result = []
# while user_input != 0:
#     tmp = user_input % 16
#     if tmp >= 10:
#         result.append(data[tmp])
#     else:
#         result.append(str(tmp))
#     user_input //= 16
# result.reverse()
# for i in result:
#     print(i, end='')
user_input = int(input())
print(str(hex(user_input))[2:])