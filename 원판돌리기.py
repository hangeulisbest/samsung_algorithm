import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def make_average():
    sum_board=[]
    for i in range(1,n+1):
        for j in range(m):
            if board[i][j]!='X':
                sum_board.append(board[i][j])
    if len(sum_board)==0:
        avg_board = 0
    else:
        avg_board = sum(sum_board)/len(sum_board)
    for i in range(1,n+1):
        for j in range(m):
            if board[i][j]!='X'and board[i][j]>avg_board:
                board[i][j]-=1
            elif board[i][j]!='X' and board[i][j]< avg_board:
                board[i][j]+=1


# 인접수 지워버리기
def check():
    flag = False
    for i in range(1,n+1):
        # 각 판마다 인접 확인
        for j in range(m):
            # 현재 검사하려는 숫자
            cur = board[i][j]
            if cur != 'X':
                q = deque([[i,j]])
                while q:
                    x,y = q.popleft()
                    for _ in range(4):
                        ni,nj = x + dx[_],(y+dy[_])%(m)
                        if 1<=ni<=n and board[ni][nj]!='X' and board[ni][nj]==cur:
                            flag = True
                            board[ni][nj]='X'
                            board[i][j]='X'
                            q.append([ni,nj])

    return flag

# xi 의 배수를 di 방향으로 ki 칸 회전하라
# di:0 시계  di:1 반시계

def rotate(xi,di,ki):
    for i in range(xi,n+1,xi):
        #반시계
        if di:
            for _ in range(ki):
                board[i].append(board[i].popleft())
        #시계
        else:
            for _ in range(ki):
                board[i].appendleft(board[i].pop())

    if not check():
        make_average()

n,m,t = map(int,input().split())
board = [deque(list(map(int,input().split()))) for _ in range(n)]
board.insert(0,[-1])

for _ in range(t):
    xi,di,ki = map(int,input().split())
    rotate(xi,di,ki)

ans = 0
for i in range(1,n+1):
    for j in range(m):
        if board[i][j]!='X':
            ans += board[i][j]
print(ans)