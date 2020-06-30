import sys
sys.stdin = open("input.txt","r")

testCase = int(input())

def rotate(a):
    n = len(a)
    tmp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[i][j]= a[n-j-1][i]
    return tmp

for tc in range(1,testCase+1):
    n = int(input())
    a = [list(map(int,input().split())) for _ in range(n)]
    ans= [ ""  for _ in range(n)]
    for _ in range(3):
        a = rotate(a)
        for i in range(n):
            for num in a[i]:
                ans[i] +=str(num)
            if _ < 2:
                ans[i]+=' '
    print("#{}".format(tc))
    for an in ans:
        print(an)
