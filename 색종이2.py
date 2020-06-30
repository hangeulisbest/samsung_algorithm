import sys
input = sys.stdin.readline

board = [list(map(int,input().split())) for _ in range(10)]
paper=[0,0,0,0,0,0]
ans = 100

def check():
    for i in range(10):
        for j in range(10):
            if board[i][j]==1:
                return False
    return True

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

def dfs(idx):
    global ans
    if idx==100:
        if check():
            ans = min(ans,sum(paper))
        return
    if ans < sum(paper):
        return
    r,c = idx//10,idx%10
    if board[r][c]==1:
        for pad in range(5,0,-1):
            if is_cover(r,c,pad):
                paper[pad]+=1
                cover(r,c,pad,0)
                dfs(idx+1)
                cover(r,c,pad,1)
                paper[pad]-=1
    else:
        dfs(idx+1)

dfs(0)
print(ans if ans!=100 else -1)
