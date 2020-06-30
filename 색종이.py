import sys
input = sys.stdin.readline

def is_cover(x,y,pad):
    if paper[pad]==5:
        return False
    for i in range(x,x+pad):
        for j in range(y,y+pad):
            if not (0<=i<10 and 0<=j<10 and board[i][j]==1):
                return False
    return True

def cover(x,y,pad,t):
    for i in range(x,x+pad):
        for j in range(y,y+pad):
            board[i][j]=t

def check():
    for i in range(10):
        for j in range(10):
            if board[i][j]==1:
                return False
    return True

def dfs(idx):
    global ans
    if idx==100:
        if check():
            ans = min(ans,sum(paper[1:]))
        return

    if ans < sum(paper[1:]):
        return
    else:
        r = idx// 10
        c = idx % 10
        if board[r][c]==1:
            for p in range(5,0,-1):
                if is_cover(r,c,p):
                    cover(r,c,p,0)
                    paper[p]+=1
                    dfs(idx+1)
                    paper[p]-=1
                    cover(r,c,p,1)
        else:
            dfs(idx+1)


ans = 26
board = [list(map(int,input().split())) for _ in range(10)]
paper = [-1,0,0,0,0,0]
dfs(0)
print(ans if ans!=26 else -1)