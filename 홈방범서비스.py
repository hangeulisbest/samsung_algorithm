import sys
sys.stdin = open("input.txt","r")

from collections import deque
testCase = int(input())

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def getBenefit(houseCnt,pay,k):
    return houseCnt*pay - (k*k+(k-1)*(k-1))

def expandBoard(n,board):
    tmp = [[0 for _ in range(n*3)] for _ in range(n*3)]
    for i in range(n,n*2):
        for j in range(n,n*2):
            tmp[i][j] = board[i-n][j-n]
    return tmp

def getDist(i,j,_i,_j):
    return abs(i-_i)+abs(j-_j)

def search(i,j,k,board,n):
    cnt = 0
    q = deque([])
    visited = [[0 for _ in range(n*3)] for _ in range(n*3)]
    visited[i][j]=1
    if board[i][j]==1:
        cnt+=1
    q.append([i,j])

    while q:
        x,y = q.popleft()

        for dir in range(4):
            tx = x + dx[dir]
            ty = y + dy[dir]
            if n<=tx<n*2 and n<=ty<n*2 and visited[tx][ty]==0 and getDist(i,j,tx,ty)< k:
                visited[tx][ty]=1
                q.append([tx,ty])
                if board[tx][ty]==1:
                    cnt+=1
    return cnt


for tc in range(1,testCase+1):
    n,pay = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    board = expandBoard(n,board)
    maxK = n if n%2!=0 else n+1
    ans,flag = 0,False

    for k in range(maxK,0,-1):
        for i in range(n,2*n):
            for j in range(n,2*n):
                houseCnt = search(i,j,k,board,n)
                if getBenefit(houseCnt,pay,k) > 0 and ans < houseCnt:
                    flag = True
                    ans = houseCnt
        if flag:
            break

    print(ans)
