from _collections import deque
def balance(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            count -= 1
    if count == 0:
        return True
    else:
        return False

def check(p):
    lst = list(p)
    stack = deque()
    while lst:
        char = lst.pop(-1)
        if char == ')':
            stack.append(char)
        else:
            if stack:
                stack.popleft()
            else:
                return False
    if stack:
        return False
    else:
        return True

def solution(p):
    if check(p):
        return p
    else:
        index = 2
        while True:
            u = p[:index]
            v = p[index:]
            if balance(u):
                break
            index += 2
        if check(u):
            answer = u + solution(v)
        else:
            answer = '('
            answer += solution(v)
            answer += ')'
            u = list(u[1:-1])
            for i in range(len(u)):
                if u[i] == '(':
                    u[i] = ')'
                else:
                    u[i] = '('
            answer += "".join(u)
        return answer


print(solution(")("))
