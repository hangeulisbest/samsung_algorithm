import sys
sys.stdin = open("input.txt","r")

from collections import defaultdict

num_dict = defaultdict(int)
testCase = int(input())

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dfs(idx,x,y,numlist,a):
    if idx==7:
        string = ''
        for num in numlist:
            string += str(num)
        num_dict[string]+=1

    else:
        for i in range(4):
            nx,ny = x + dx[i],y+dy[i]
            if 0<=nx<4 and 0<=ny<4:
                numlist.append(a[nx][ny])
                dfs(idx+1,nx,ny,numlist,a)
                numlist.pop()


for tc in range(1,testCase+1):
    a = [list(map(int,input().split())) for _ in range(4)]
    num_dict=defaultdict(int)
    for i in range(4):
        for j in range(4):
            dfs(0,i,j,[],a)
    print('#{} {}'.format(tc,len(num_dict)))
