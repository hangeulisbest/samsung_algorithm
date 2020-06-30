import sys
from collections import deque
from copy import deepcopy
sys.stdin = open("input.txt","r")

testCase = int(input())
INF = 987654321
ans = INF

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def Shoot(arr,line):
    # 0<= line < w
    w,h = len(arr[0]),len(arr)
    st=[-1,line]
    arr = deepcopy(arr)
    for i in range(h):
        if arr[i][line] != 0:
            st[0]=i
            break

    if st[0]<0:
        return arr
    ch = [[0 for _ in range(w)] for _ in range(h)]
    q = deque([st])
    ch[st[0]][st[1]]=1

    # bfs check
    while q:
        x,y = q.popleft()

        for i in range(4):
            tx,ty = x,y
            for _ in range(arr[x][y]-1):
                tx +=dx[i]
                ty +=dy[i]
                if 0<=tx<h and 0<=ty<w and ch[tx][ty]==0:
                    ch[tx][ty]=1
                    q.append([tx,ty])
        arr[x][y]=0

    # remove Blank
    for i in range(w):
        tmp = []
        for j in range(h):
            if arr[j][i]!=0:
                tmp.append(arr[j][i])
        for j in range(h-1,-1,-1):
            if len(tmp)==0:
                arr[j][i]=0
            else:
                arr[j][i]=tmp.pop()

    return arr


def FindMinBlock(idx,n,w,h,arr):
    global ans
    if idx==n:
        cnt =0
        for i in range(h):
            for j in range(w):
                if arr[i][j]>0:
                    cnt+=1
        if cnt < ans:
            ans = cnt
    else:
        for i in range(w):
            FindMinBlock(idx+1,n,w,h,Shoot(arr,i))



for tc in range(1,testCase+1):
    n,w,h=map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(h)]

    FindMinBlock(0,n,w,h,arr)

    print("#{} {}".format(tc,ans))
    ans = INF
