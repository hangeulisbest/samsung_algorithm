import sys
sys.stdin = open("input.txt","r")

testCase = int(input())


def check(arr,x):
    tmp,cnt = arr[0],1
    cntlist=[]
    for i in range(1,len(arr)):
        if arr[i]!=tmp:
            if abs(arr[i]-tmp)>1:
                return False
            cntlist.append(cnt)
            cnt=1
            if arr[i]-tmp < 0:
                cntlist.append('D')
            else:
                cntlist.append('U')
        else:
            cnt+=1
        tmp = arr[i]
    else:
        cntlist.append(cnt)
    for i in range(len(cntlist)):
        if cntlist[i]=='D':
            if cntlist[i+1] < x:
                return False
            cntlist[i+1]-=x
        elif cntlist[i]=='U':
            if cntlist[i-1] < x:
                return False
            cntlist[i-1]-=x

    return True



for tc in range(1,testCase+1):
    n,x = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(n)]

    ans=0

    for i in range(n):
        row,col=[],[]
        for j in range(n):
            row.append(a[i][j])
            col.append(a[j][i])

        if check(row,x):
            ans+=1
        if check(col,x):
            ans+=1


    print("#{} {}".format(tc,ans))