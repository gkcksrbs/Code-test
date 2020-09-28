S = input()

result = 0

for i in S:
    if int(i) == 1 or int(i) == 0:
        result += int(i)
    else:
        if result == 0:
            result += int(i)
        else:
            result *= int(i)

print(result)