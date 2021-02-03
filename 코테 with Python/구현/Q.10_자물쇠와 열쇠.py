def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            ret[j][N-1-i] = m[i][j]

    return ret

def check(new_lock):
    lock_length = len(new_lock) // 3

    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = n
    m = len(key)
    new_lock = [[0]*(n*3) for _ in range(n*3)]

    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]

    for rotate in range(4):
        key = rotate_90(key)

        for x in range(n*2):
            for y in range(n*2):

                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]

                if check(new_lock) == True:
                    return True

                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False
print(solution([[0,0,0],[1,0,0],[0,1,1]],[[1,1,1],[1,1,0],[1,0,1]]))

