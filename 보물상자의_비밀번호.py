import sys
sys.stdin = open("input.txt","r")

from collections import deque
testCase = int(input())

for tc in range(1,testCase+1):
    n,k = map(int,input().split())
    a = list(input().rstrip())

    x = n//4
    d = {}
    for _ in range(x):
        for i in range(0,n,x):
            string = ''.join(a[i:i+x])
            d[string] = int(string,16)
        a = deque(a)
        a.append(a.popleft())
        a=list(a)
    anslist = sorted(d.items(),key=lambda x:x[1],reverse=True)
    print("#{} {}".format(tc,anslist[k-1][1]))