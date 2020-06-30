import sys
sys.stdin = open("input.txt","r")

import copy
testCase = int(input())

ans = 987654321

def check(a,k):
    d,w = len(a),len(a[0])
    for i in range(w):
        tmp = [a[0][i],1]
        for j in range(1,d):
            if tmp[0] == a[j][i]:
                tmp[1]+=1
                if tmp[1]>=k:
                    break
            else:
                tmp[0],tmp[1] = a[j][i],1
        else:
            return False
    return True

def dfs(idx,k,a,cnt):
    global ans
    if idx == len(a):
        if check(a,k):
            if ans > cnt:
                ans = cnt
    else:
        dfs(idx+1,k,a,cnt)
        if cnt+1 < k:
            tmp = [ x for x in a[idx]]

            for i in range(len(a[idx])):
                a[idx][i] = 0
            dfs(idx+1,k,a,cnt+1)

            for i in range(len(a[idx])):
                a[idx][i] = 1
            dfs(idx+1,k,a,cnt+1)

            for i in range(len(a[idx])):
                a[idx][i] = tmp[i]




for tc in range(1,testCase+1):
    d,w,k = map(int,input().split())
    a = [ list(map(int,input().split())) for _ in range(d)]
    ans = k
    dfs(0,k,a,0)
    if k==1:
        print('#{} {}'.format(tc,0))
    else:
        print("#{} {}".format(tc,ans))

