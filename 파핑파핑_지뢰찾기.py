import sys
sys.stdin = open("input.txt","r")

from collections import deque
testCase = int(input())

dx=[0,0,-1,1,-1,-1,1,1]
dy=[1,-1,0,0,1,-1,1,-1]

def ret_num(x,y):
    res = 0
    for i in range(8):
        nx,ny = x + dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n and a[nx][ny]=='*':
            res+=1
    return res


def bfs(x,y,ch):
    ch[x][y]=1
    q = deque([])
    q.append([x,y])

    while q:
        x,y = q.popleft()

        for i in range(8):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and ch[nx][ny]==0 and a[nx][ny]!='*':
                ch[nx][ny]=1
                if a[nx][ny]==0:
                    q.append([nx,ny])



def count_a():
    ch = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if a[i][j]==0 and ch[i][j]==0:
                bfs(i,j,ch)
                cnt +=1

    for i in range(n):
        for j in range(n):
            if str(a[i][j]).isdecimal() and a[i][j]>0 and ch[i][j]==0:
                cnt += 1

    return cnt

for tc in range(1,testCase+1):
    n = int(input())
    a = [list(map(str,input().rstrip())) for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(n):
            if a[i][j]=='.':
                a[i][j] = ret_num(i,j)

    ans = count_a()
    print('#{} {}'.format(tc,ans))


