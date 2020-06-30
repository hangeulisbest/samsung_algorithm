import sys
sys.stdin= open("input.txt","r")

testCase = int(input())

for tc in range(1,testCase+1):
    n,m=map(int,input().split())
    a = []
    low,high=1,0
    for _ in range(n):
        tmp = int(input())
        if tmp > high:
            high = tmp
        a.append(tmp)
    high = high * m
    ans = high
    while low <= high:
        mid = (low + high) // 2
        sum_p=0
        for k in a:
            sum_p += mid//k


        if sum_p >= m:
            high = mid -1
            ans = mid
        else:
            low = mid + 1

    print('#{} {}'.format(tc,ans))

