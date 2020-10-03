Input = input()
tmp_1 = Input[0:len(Input)//2]
tmp_2 = Input[len(Input)//2:len(Input)]

lst_1, lst_2 = [], []

for i in tmp_1:
    lst_1.append(int(i))

for i in tmp_2:
    lst_2.append(int(i))

if sum(lst_1) == sum(lst_2):
    print('LUCKY')
else:
    print('READY')
