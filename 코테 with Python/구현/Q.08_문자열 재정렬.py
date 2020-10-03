Str = list(input())
Str.sort()

Sum = 0
result = ''

for i in Str:
    if i.isalpha():
        result += i
    else:
        Sum += int(i)

result += str(Sum)

print(result)