def check(result):
    for x, y, st in result:
        if st == 0:
            if y == 0 or [x-1, y, 1] in result or [x, y-1, 0] in result or [x, y, 1] in result:
                continue
            return False
        elif st == 1:
            if [x, y-1, 0] in result or [x+1, y-1, 0] in result or ([x-1, y, 0] in result and [x+1, y, 0] in result):
                continue
            return False
    return True

def solution(n, build_frame):
    result = []

    for i in build_frame:
        x, y, st, op = i

        if op == 0:
            result.remove([x, y, st])
            if not check(result):
                result.append([x, y, st])
        if op == 1:
            result.append([x, y, st])
            if not check(result):
                result.remove([x, y, st])

    return sorted(result)

print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
