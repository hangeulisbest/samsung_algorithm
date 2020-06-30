
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

testCase = int(input())
def isExpandible(n,m,a):
    expandible = False
    for i in range(n):
        if a[i][0][1]!=0 and a[i][0][0]==a[i][0][1]:
            expandible = True
            break
        if a[i][m-1][1]!=0 and a[i][m-1][0]==a[i][m-1][1]:
            expandible = True
            break
    for j in range(m):
        if a[0][j][1]!=0 and a[0][j][0] == a[0][j][1]:
            expandible = True
            break
        if a[n-1][j][1]!=0 and a[n-1][j][0] == a[n-1][j][1]:
            expandible = True
            break
    return expandible

def expandMap(n,m,a):
    row,col = len(a[0]),len(a)
    if isExpandible(n,m,a):
        tmp = [[[0,0] for _ in range(row*3)] for _ in range(col*3)]
        for i in range(col,col*2):
            for j in range(row,row*2):
                tmp[i][j] = [a[i-col][j-row][0],a[i-col][j-row][1]]
        return n*3,m*3,tmp
    else:
        return n,m,a

def oneStep(n,m,a):
    n,m,a = expandMap(n,m,a)
    q = deque([])
    for i in range(n):
        for j in range(m):
            r,s = a[i][j][0],a[i][j][1]
            if r>s:
                a[i][j] = [r-1,s]
            elif r>0 and r<=s:
                a[i][j] = [r-1,s]
                q.append([i,j])
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if (a[tx][ty][0]!=0 and a[tx][ty][0]==a[tx][ty][1]*2 and a[tx][ty][1] < a[x][y][1]) or (a[tx][ty][1]==0):
                a[tx][ty]=[a[x][y][1]*2,a[x][y][1]]
            
    return n,m,a
                
            
    

for tc in range(1,testCase+1):
    n,m,k=map(int,input().split())
    a = []
    for _ in range(n):
        tmp,line = [],list(map(int,input().split()))
        for l in line:
            tmp.append([l*2,l])
        a.append(tmp)
    
    for _ in range(k):
        n,m,a = oneStep(n,m,a)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if a[i][j][0]>0:
                cnt+=1
    print("#{} {}".format(tc,cnt))
        
    

