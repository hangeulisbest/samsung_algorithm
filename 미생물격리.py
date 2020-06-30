import sys
sys.stdin = open("input.txt","r")


from collections import deque
testCase = int(input())

dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]

def move(a):
    n = len(a)
    q = deque([])
    for i in range(n):
        for j in range(n):
            if len(a[i][j]) >0:
                q.append([i,j])
    while q:
        x,y = q.popleft()

        a[x][y] = [ a[x][y][r] for r in range(len(a[x][y])-1,-1,-1)]
        num,dir = a[x][y].pop()

        tx = x + dx[dir]
        ty = y + dy[dir]
        a[tx][ty].append([num,dir])


def check(a):
    n=len(a)
    for i in range(n):
        if len(a[0][i]) >0:
            num,dir = a[0][i].pop()
            num = num // 2
            dir = dir-1 if dir%2==0 else dir+1
            a[0][i].append([num,dir])
        if len(a[n-1][i]) >0:
            num,dir = a[n-1][i].pop()
            num = num // 2
            dir = dir-1 if dir%2==0 else dir+1
            a[n-1][i].append([num,dir])
    for i in range(1,n-1):
        if len(a[i][0]) >0:
            num,dir = a[i][0].pop()
            num = num // 2
            dir = dir-1 if dir%2==0 else dir+1
            a[i][0].append([num,dir])
        if len(a[i][n-1]) >0:
            num,dir = a[i][n-1].pop()
            num = num // 2
            dir = dir-1 if dir%2==0 else dir+1
            a[i][n-1].append([num,dir])

    for i in range(1,n-1):
        for j in range(1,n-1):
            if len(a[i][j]) > 0:
                num,dir = a[i][j][0][0],a[i][j][0][1]
                max_num = num
                for r in range(1,len(a[i][j])):
                    if a[i][j][r][0] > max_num:
                        max_num = a[i][j][r][0]
                        dir = a[i][j][r][1]
                    num += a[i][j][r][0]
                a[i][j] = [[num,dir]]



for tc in range(1,testCase+1):
    n,m,k = map(int,input().split())
    a = [[[] for _ in range(n)] for _ in range(n)]
    ans = 0
    for _ in range(k):
        x,y,num,dir = map(int,input().split())
        a[x][y].append([num,dir])

    for _ in range(m):
        move(a)
        check(a)

    for i in range(n):
        for j in range(n):
            if len(a[i][j])==1:
                ans += a[i][j][0][0]


    print("#{} {}".format(tc,ans))

