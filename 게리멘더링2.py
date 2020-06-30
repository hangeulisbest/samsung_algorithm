# 5개의 선거구로 나눠야 한다.
# 선거구는 적어도 하나를 포함
# 한 선거구의 지역은 모두 연결
# 중간에 통하는 인접한 구역은 0개 이

import sys
input = sys.stdin.readline
from collections import deque
dx = [0,0,-1,1]
dy = [1,-1,0,0]
ans = 987654321
def check_make_5_loc(x,y,d1,d2):
    # 경계선1
    for i in range(d1 + 1):
        if not (1<=x+i<=n and 1<=y-i<=n):
            return False
    # 경계선2
    for i in range(d2 + 1):
        if not (1 <= x + i <= n and 1 <= y + i <= n):
            return False
    # 경계선3
    for i in range(d2 + 1):
        if not (1 <= x + d1 + i <= n and 1 <= y - d1 + i <= n):
            return False
    # 경계선4
    for i in range(d1 + 1):
        if not (1 <= x + d2 + i <= n and 1 <= y + d2 - i <= n):
            return False
    return True

def get_sub(area):
    ingu=[0]*5

    for i in range(1,n+1):
        for j in range(1,n+1):
            ingu[area[i][j]-1]+=people[i][j]

    ingu.sort()
    return ingu[-1]-ingu[0]

def div_area(d1,d2):
    global ans
    for x in range(1,n+1):
        for y in range(1,n+1):
            area = [[0] * (n + 1) for _ in range(n+1)]
            if x+d1+d2<=n and y-d1<y and y+d2<=n and check_make_5_loc(x,y,d1,d2):
                # 경계선1
                for i in range(d1+1):
                    area[x+i][y-i]=5
                # 경계선2
                for i in range(d2+1):
                    area[x+i][y+i]=5
                # 경계선3
                for i in range(d2+1):
                    area[x+d1+i][y-d1+i]=5
                # 경계선4
                for i in range(d1+1):
                    area[x+d2+i][y+d2-i]=5

                # 5번 채우기
                for i in range(x,n+1):
                    for j in range(1,n+1):
                        if area[i][j]==5:
                            for k in range(j+1,n+1):
                                if area[i][k]==5:
                                    for u in range(j,k+1):
                                        area[i][u]=5

                # 1번 선거구
                for i in range(1,x+d1):
                    for j in range(1,y+1):
                        if area[i][j] == 0:
                            area[i][j]=1
                # 2번 선거구
                for i in range(1,x+d2+1):
                    for j in range(y+1,n+1):
                        if area[i][j]==0:
                            area[i][j]=2
                # 3번 선거구
                for i in range(x+d1,n+1):
                    for j in range(1,y-d1+d2):
                        if area[i][j] == 0:
                            area[i][j]=3
                # 4번 선거구
                for i in range(x+d2+1,n+1):
                    for j in range(y-d1+d2,n+1):
                        if area[i][j] == 0:
                            area[i][j]=4

                tmp=get_sub(area)
                if tmp < ans:
                    ans = tmp

n=int(input())
people=[[0]*(n+1)]
for _ in range(n):
    tmp = list(map(int,input().split()))
    tmp.insert(0,0)
    people.append(tmp)

for _d1 in range(1,n):
    for _d2 in range(1,n):
        div_area(_d1,_d2)
print(ans)


