import sys
sys.stdin = open("input.txt","r")

from collections import deque

dx = [0,0,1,0,-1]
dy = [0,-1,0,1,0]
testCase = int(input())

def bfs(x,y,c,p,idx,board,idx2charge):
    ch = [[0 for _ in range(11)] for _ in range(11)]
    board[y][x].append(idx)
    idx2charge[idx] = p
    ch[y][x]=1
    base = [y,x]
    q = deque([[y,x]])

    while q:
        y,x = q.popleft()

        for i in range(1,5):
            ty = y + dy[i]
            tx = x + dx[i]
            dist  = abs(ty-base[0])+abs(tx-base[1])
            if 1<=ty<=10 and 1<=tx<=10 and ch[ty][tx]==0 and dist <= c:
                ch[ty][tx]=1
                board[ty][tx].append(idx)
                q.append([ty,tx])

def charging(aloc,bloc,board,idx2charge,ans):
    ax,ay = aloc[0],aloc[1]
    bx,by = bloc[0],bloc[1]
    ascope = [ x for x in board[ay][ax]]
    bscope = [ x for x in board[by][bx]]
    if len(ascope) >0 and len(bscope) >0:
        max_tmp = -1
        for i in range(len(ascope)):
            for j in range(len(bscope)):
                if ascope[i]==bscope[j]:
                    tmp = idx2charge[ascope[i]]
                else:
                    tmp = idx2charge[ascope[i]]
                    tmp += idx2charge[bscope[j]]
                if max_tmp < tmp:
                    max_tmp = tmp
        ans += max_tmp
    else:
        max_tmp = -1
        for i in range(len(ascope)):
            if idx2charge[ascope[i]] > max_tmp:
                max_tmp = idx2charge[ascope[i]]
        if max_tmp!=-1:
            ans += max_tmp
        max_tmp=-1
        for i in range(len(bscope)):
            if idx2charge[bscope[i]] > max_tmp:
                max_tmp = idx2charge[bscope[i]]
        if max_tmp !=-1:
            ans+= max_tmp
    return ans
for tc in range(1,testCase+1):
    m,a = map(int,input().split())
    board = [ [[] for _ in range(11)] for _ in range(11)]
    atrk = list(map(int,input().split()))
    btrk = list(map(int,input().split()))
    atrk = [0] + atrk
    btrk = [0] + btrk
    idx2charge = {}
    for idx in range(1,a+1):
        x,y,c,p = map(int,input().split())
        bfs(x,y,c,p,idx,board,idx2charge)

    aloc = [1,1]
    bloc = [10,10]
    ans = 0
    for i in range(len(atrk)):
        aloc[0] += dx[atrk[i]]
        aloc[1] += dy[atrk[i]]
        bloc[0] += dx[btrk[i]]
        bloc[1] += dy[btrk[i]]
        ans = charging(aloc,bloc,board,idx2charge,ans)
    print("#{} {}".format(tc,ans))
