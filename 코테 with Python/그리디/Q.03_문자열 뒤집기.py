S = input()
lst = list(S)

make_zero = 0
make_one = 0

if S[0] == '1':
    make_zero += 1
else:
    make_one += 1

for i in range(len(S) - 1):
    if S[i] != S[i+1]:
        if S[i+1] == '1':
            make_zero += 1
        else:
            make_one += 1

print(min(make_zero, make_one))