from _collections import deque

def solution(s):
    if len(s) == 1:
        len_lst = [0]
    else:
        len_lst = [0 for _ in range(len(s)//2)]

    for i in range(len(len_lst)):
        lst = deque(s[j:j + i+1] for j in range(0, len(s), i+1))
        result = ''

        while len(lst) != 0:
            alpha = lst.popleft()
            count = 1

            while True:
                if len(lst) != 0 and lst[0] == alpha:
                    lst.popleft()
                    count += 1
                else:
                    break

            if count != 1:
                result += str(count)
            result += alpha

        len_lst[i] = len(result)

    return min(len_lst)

print(solution('a'))