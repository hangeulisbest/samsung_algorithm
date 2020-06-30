import sys
sys.stdin = open("input.txt", "r")

def nextLoc(x,y,board,dir,wHole,cnt):
    reverseDir = {0:2,1:3,2:0,3:1}
    tx = x + dx[dir]
    ty = y + dy[dir]
    if board[tx][ty]==0:
        return tx,ty,dir,cnt
    elif board[tx][ty]==-1:
        return -1,-1,-1,cnt
    elif 1<=board[tx][ty]<=5:
        if (board[tx][ty]==1 and dir==3) or (board[tx][ty]==1 and dir==2):
            if dir==3:
                return tx,ty,0,cnt+1
            else:
                return tx,ty,1,cnt+1
        elif (board[tx][ty]==2 and dir==3) or (board[tx][ty]==2 and dir==0):
            if dir==3:
                return tx,ty,2,cnt+1
            else:
                return tx,ty,1,cnt+1
        elif (board[tx][ty]==3 and dir==1) or (board[tx][ty]==3 and dir==0):
            if dir==1:
                return tx,ty,2,cnt+1
            else:
                return tx,ty,3,cnt+1
        elif (board[tx][ty]==4 and dir==1) or (board[tx][ty]==4 and dir==2):
            if dir==1:
                return tx,ty,0,cnt+1
            else:
                return tx,ty,3,cnt+1
        else:
            return tx,ty,reverseDir[dir],cnt+1
    else:
        string ='{} {}'.format(tx,ty)
        wx,wy = map(int,wHole[string].split())
        return wx,wy,dir,cnt


def move(i,j,board,dir,wHole):
    st = [i,j]
    cnt = 0
    x,y=i,j
    while True:
        x,y,dir,cnt=nextLoc(x,y,board,dir,wHole,cnt)
        if x==st[0] and y==st[1]:
            break
        if x==-1:
            break
    return cnt

# 상 우 하 좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

testCase = int(input())

for tc in range(1,testCase+1):
    n = int(input())
    board = [[5]*(n+1)]
    for _ in range(n):
        tmp = list(map(int,input().split()))
        tmp.insert(0,5)
        tmp.append(5)
        board.append(tmp)
    board.append([5]*(n+1))
    wHole = {}
    for i in range(1,n+1):
        for j in range(1,n+1):
            if board[i][j]>=6:
                if board[i][j] in wHole:
                    wHole[wHole[board[i][j]]]='{} {}'.format(i,j)
                    wHole['{} {}'.format(i,j)]=wHole[board[i][j]]
                else:
                    wHole[board[i][j]]='{} {}'.format(i,j)

    ans = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if board[i][j]==0:
                for k in range(4):
                    tmp = move(i,j,board,k,wHole)
                    if tmp > ans:
                        ans = tmp

    print('#{} {}'.format(tc,ans))
