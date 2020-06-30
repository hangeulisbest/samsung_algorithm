import sys
sys.stdin = open("input.txt","r")


testCase = int(input())


def making(n):
    res = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if i+j+k==n:
                    res.append([i,j,k])
    return res

def ret_cnt(rge,a,f):
    cnt = 0
    for i in range(rge[0],rge[1]):
        for j in range(m):
            if a[i][j]!=f:
                cnt += 1
    return cnt

def count_tile(row,a):
    m = len(a[0])
    w_rge = [0,row[0]]
    b_rge = [row[0],row[0]+row[1]]
    r_rge = [row[0]+row[1],row[0]+row[1]+row[2]]
    cnt = 0
    cnt += ret_cnt(w_rge,a,'W')
    cnt += ret_cnt(b_rge,a,'B')
    cnt += ret_cnt(r_rge,a,'R')

    return cnt

for tc in range(1,testCase+1):
    n,m = map(int,input().split())
    a = [list(map(str,input().rstrip())) for _ in range(n)]
    ans = 987654321
    for candi in making(n):
        c = count_tile(candi,a)
        if c < ans:
            ans = c

    print('#{} {}'.format(tc,ans))
