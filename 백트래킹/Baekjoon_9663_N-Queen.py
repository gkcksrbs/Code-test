N = int(input())

check = [[False for j in range(N)] for i in range(N)]
lst = []
def N_Queen(index):
    tmp = []
    if(index == N):
        print(len(lst))
        return
    for i in range(N):
        for j in range(N):
            if check[i][j]:
                continue
            tmp.append(j)
            for k in range(i, N):
                check[i][k] = True
            for k in range(N-1-i, N):
                check[i][N-1-k] = True
            for k in range(i, N):
                check[k][j] = True
            for k in range(N-j):
                try:
                    check[i+k][j+k] = True
                except:
                    continue
            for k in range(i, j):
                try:
                    check[i+k][j-k] = True
                except:
                    continue
            N_Queen(index+1)
N_Queen(0)
# print(check)
# print(tmp)