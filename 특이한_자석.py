import sys
sys.stdin = open("input.txt","r")

from collections import deque

testCase = int(input())

#1
def Rotate(arr):
    tmp = deque([x for x in arr])
    tmp.appendleft(tmp.pop())
    return tmp

#-1
def RevRotate(arr):
    tmp = deque([x for x in arr])
    tmp.append(tmp.popleft())
    return tmp

def Do(num,dir,a,v):
    if num<0 or num>3 or v[num]==1:
        return

    v[num]=1
    #left check
    if num-1>=0 and a[num][6]+a[num-1][2]==1 and v[num-1]==0:
        Do(num-1,dir*(-1),a,v)

    #right check
    if num+1<=3 and a[num][2]+a[num+1][6]==1 and v[num+1]==0:
        Do(num+1,dir*(-1),a,v)

    if dir<0:
        a[num] = RevRotate(a[num])
    else:
        a[num] = Rotate(a[num])


for tc in range(1,testCase+1):
    k=int(input())
    a = [deque(list(map(int,input().split()))) for _ in range(4)]

    for _ in range(k):
        num,dir=map(int,input().split())
        Do(num-1,dir,a,[0,0,0,0])

    ans  = sum([1*a[0][0],2*a[1][0],4*a[2][0],8*a[3][0]])

    print("#{} {}".format(tc,ans))
