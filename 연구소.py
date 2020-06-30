import sys
input = sys.stdin.readline

from itertools import combinations as comb
from collections import deque

n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
#바이러스 위치
v_idx=[]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

# v_idx 중에서 *가 아닌 것들을 m개를 bfs 돌리자
def bfs_check():
    q = deque([])
    ch = [[0 for _ in range(n)] for _ in range(n)]
    for v in v_idx:
        if a[v[0]][v[1]]==2:
            q.append([v[0],v[1],0])
    tmp_ans = 0
    while q:
        x,y,cnt = q.popleft()

        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and ch[nx][ny]==0 and (a[nx][ny]==0 or a[nx][ny]=='*'):
                ch[nx][ny]=1
                q.append([nx,ny,cnt+1])
                if a[nx][ny]==0:
                    tmp_ans=cnt+1

    for i in range(n):
        for j in range(n):
            if a[i][j]==0 and ch[i][j]==0:
                return 987654321
    return tmp_ans
for i in range(n):
    for j in range(n):
        if a[i][j]==2:
            v_idx.append([i,j])
ans = 987654321
for c in comb(v_idx,len(v_idx)-m):
    for cc in c:
        a[cc[0]][cc[1]]='*'
    tmp = bfs_check()
    if tmp < ans:
        ans = tmp
    for cc in c:
        a[cc[0]][cc[1]]=2
if ans ==987654321:
    print(-1)
else:
    print(ans)
