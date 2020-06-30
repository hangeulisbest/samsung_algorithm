import sys
sys.stdin = open("input.txt","r")

dx = [0,0,1,-1,1,1,-1,-1]
dy = [-1,1,0,0,1,-1,-1,1]

testCase = int(input())

for tc in range(1,testCase+1):
    n,m=map(int,input().split())
    board=[[0 for _ in range(n)] for _ in range(n)]
    mid=(n+1)//3

    board[mid][mid],board[mid+1][mid+1]=2,2
    board[mid+1][mid],board[mid][mid+1]=1,1


    for _ in range(m):
        x,y,k = map(int,input().split())
        x,y=y-1,x-1
        board[x][y]=k
        for i in range(8):
            tx,ty=x,y
            flag=False
            while True:
                tx+=dx[i]
                ty+=dy[i]
                if 0>tx or n<=tx or 0>ty or n<=ty or board[tx][ty]==0:
                    break
                if board[tx][ty]==k:
                    flag=True
                    break

            if flag:
                tmpx,tmpy=x,y
                while tmpx!=tx or tmpy!=ty:
                    board[tmpx][tmpy] = k
                    tmpx+=dx[i]
                    tmpy+=dy[i]

    black,white=0,0
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                black+=1
            elif board[i][j]==2:
                white+=1
    print("#{} {} {}".format(tc,black,white))