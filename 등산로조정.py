import sys
sys.stdin = open("input.txt","r")

testCase = int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = 1

def search(a,loc,track,k,isCut):
    global ans
    x,y=loc[0],loc[1]
    if len(track)>ans:
        ans = len(track)
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<len(a) and 0<=ny<len(a) and (not ([nx,ny] in track)):
            gab = a[x][y] - a[nx][ny]
            if gab>0:
                track.append([nx,ny])
                search(a,[nx,ny],track,k,isCut)
                track.pop()
            elif -1*k<gab<=0 and isCut==False:
                track.append([nx,ny])
                tmp = a[nx][ny]
                a[nx][ny]=a[x][y]-1
                search(a,[nx,ny],track,k,True)
                a[nx][ny]=tmp
                track.pop()








for tc in range(1,testCase+1):
    n,k = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(n)]
    ans = 0
    st = []

    st_point = 0
    for i in range(n):
        for j in range(n):
            if a[i][j]>= st_point:
                st_point = a[i][j]

    for i in range(n):
        for j in range(n):
            if a[i][j]==st_point:
                st.append([i,j])


    for s in st:
        search(a,s,[[s[0],s[1]]],k,False)

    print("#{} {}".format(tc,ans))
