import sys
sys.stdin = open("input.txt","r")

from copy import deepcopy
testCase = int(input())

pCase=[]
def MakepCase(idx,tmp,people,lenp,stairdist):
    if idx==lenp:
        pCase.append(deepcopy(tmp))
    else:
        for i in range(2):
            tmp.append([0,people[idx][i]+stairdist[i],i])
            MakepCase(idx+1,tmp,people,lenp,stairdist)
            tmp.pop()
def check(case):
    for c in case:
        if c[0]<=c[1]:
            return True
    return False

for tc in range(1,testCase+1):
    n=int(input())
    a= [list(map(int,input().split())) for _ in range(n)]

    stairIndex,stairdist=[],[]
    for i in range(n):
        for j in range(n):
            if a[i][j]>1:
                stairIndex.append([i,j])
                stairdist.append(a[i][j])

    people=[]
    for i in range(n):
        for j in range(n):
            if a[i][j]==1:
                people.append([abs(i-stairIndex[0][0])+abs(j-stairIndex[0][1]), abs(i-stairIndex[1][0])+abs(j-stairIndex[1][1])])
    pCase=[]
    MakepCase(0,[],people,len(people),stairdist)
    ans = 987654321

    for case in pCase:
        miniute=0
        st=[0,0]
        while check(case):
            #1분 씩 증가
            waiter = []
            for i in range(len(case)):
                if case[i][0] < case[i][1]-stairdist[case[i][2]]:
                    case[i][0]+=1
                elif case[i][0] == case[i][1]-stairdist[case[i][2]]:
                    if st[case[i][2]] < 3:
                        st[case[i][2]]+=1
                        case[i][0]+=1
                    elif st[case[i][2]]==3:
                        waiter.append(i)
                elif case[i][1]-stairdist[case[i][2]] < case[i][0] <= case[i][1]:
                    case[i][0]+=1
                    if case[i][0]>case[i][1]:
                        st[case[i][2]]-=1
            for w in waiter:
                if st[case[w][2]] < 3:
                    st[case[w][2]]+=1
                    case[w][0]+=1

            miniute+=1

        if ans > miniute:
            ans = miniute
    print("#{} {}".format(tc,ans))