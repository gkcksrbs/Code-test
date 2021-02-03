from _collections import deque
# 상,하,좌,우
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def solution(board):
    robot = {(0, 0), (0, 1)}
    end = len(board) - 1
    time = 0
    visited = [robot]

    q = deque()
    q.append((robot, time))

    while q:
        r, b = q.popleft()

        if (end, end) in r:
            return b

        r1, r2 = r

        for i in range(4):
            nr1, nr2 = (r1[0] + dx[i], r1[1] + dy[i]), (r2[0] + dx[i], r2[1] + dy[i])

            if 0 <= nr1[0] <= end and 0 <= nr1[1] <= end and 0 <= nr2[0] <= end and 0 <= nr2[1] <= end:
                if {nr1, nr2} not in visited:
                    if board[nr1[0]][nr1[1]] == 0 and board[nr2[0]][nr2[1]] == 0:
                        visited.append({nr1, nr2})
                        q.append(({nr1, nr2}, b+1))

        # for i in range(2):

    return visited
print(solution([[0,0,0,1,1],[0,0,0,1,0],[0,1,0,1,1],[1,1,0,0,1],[0,0,0,0,0]]))
