import sys
sys.stdin = open("input.txt","r")


from collections import deque
testcase = int(input())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

num2dir={
    1:[[-1,0],[0,1],[1,0],[0,-1]],
    2:[[-1,0],[1,0]],
    3:[[0,-1],[0,1]],
    4:[[-1,0],[0,1]],
    5:[[1,0],[0,1]],
    6:[[1,0],[0,-1]],
    7:[[-1,0],[0,-1]]
}

def bfs(tunnel,r,c,l):
    n,m = len(tunnel),len(tunnel[0])
    ch = [[0 for _ in range(m)] for _ in range(n)]
    ch[r][c]=1
    q = deque([])
    q.append([r,c,1])

    while q:
        x,y,ti = q.popleft()

        psible_dir=num2dir[tunnel[x][y]]

        for p in psible_dir:
            nx,ny = x + p[0],y + p[1]
            cond_dir= [p[0]*-1,p[1]*-1]
            if 0<=nx<n and 0<=ny<m and ch[nx][ny]==0 and tunnel[nx][ny]>0 \
                    and ti+1<=l and (cond_dir in num2dir[tunnel[nx][ny]]):
                    ch[nx][ny]=1
                    q.append([nx,ny,ti+1])

    cnt = 0
    for c in ch:
        cnt += sum(c)
    return cnt

for tc in range(1,testcase+1):
    n,m,r,c,l = map(int,input().split())
    tunnel = [list(map(int,input().split())) for _ in range(n)]
    print('#{} {}'.format(tc,bfs(tunnel,r,c,l)))