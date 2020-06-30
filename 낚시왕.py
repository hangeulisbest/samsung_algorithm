import sys
input = sys.stdin.readline

# 상 하 우 좌
dx = [0,-1,1,0,0]
dy = [0,0,0,1,-1]

di = {}
ans = 0
def move_shark(di,r,c):
    tmp = {}
    for k,v in di.items():
        # 위치
        x,y = map(int,k.split())

        # 속력 이동방향 크기
        s,d,z = v

        # s 줄이기
        base_len = (r-1)*2 if d<3 else (c-1)*2
        s = (s % base_len)

        # move
        nx,ny = x,y
        for _ in range(s):
            tmp_nx, tmp_ny = nx + dx[d], ny + dy[d]
            if tmp_nx<1 or tmp_nx> r or tmp_ny<1 or tmp_ny> c:
                if d%2==0:
                    d -=1
                else:
                    d +=1
            nx,ny = nx+dx[d],ny+dy[d]

        # check
        string = "{} {}".format(nx,ny)
        if string in tmp:
            if tmp[string][2] > z:
                continue
        tmp[string] = [s,d,z]

    return tmp

def catch_shark(idx,r,di):
    global ans
    for i in range(1,r+1):
        string = "{} {}".format(i,idx)
        if string in di:
            ans += di[string][2]
            del di[string]
            break

r,c,m = map(int,input().split())
for _ in range(m):
    x,y,s,d,z = map(int,input().split())
    string = "{} {}".format(x,y)
    di[string]=[s,d,z]

for i in range(1,c+1):
    catch_shark(i,r,di)
    di = move_shark(di,r,c)

print(ans)