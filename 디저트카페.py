import sys
sys.stdin = open("input.txt","r")

testcase = int(input())
ans = 0
# 0:오른아래 1:왼아래 2:왼쪽위 3:오른위
dx = [1,1,-1,-1]
dy = [1,-1,-1,1]

def possible_start_point(i,j,a):
    n = len(a)
    if 0<=i+dx[0]<n and 0<=j+dy[0]<n and \
        0<=i+dx[1]<n and 0<=j+dy[1]<n:
            return True
    return False


def dfs(start_point,i,j,a,dir_list,dessert_list):
    global ans
    if len(dir_list)==4 and start_point[0]==i and start_point[1]==j:
        candi = len(dessert_list)
        if candi > ans :
            ans = candi
    else:
        present_dir = dir_list[-1]
        nx,ny = i + dx[present_dir],j+dy[present_dir]
        if 0<=nx <len(a) and 0<=ny<len(a) and ( not (a[nx][ny] in dessert_list )):
            dessert_list.append(a[nx][ny])
            dfs(start_point,nx,ny,a,dir_list,dessert_list)
            dessert_list.pop()

        if len(dir_list)<4:
            next_dir = present_dir + 1
            nx,ny = i + dx[next_dir],j+dy[next_dir]
            if 0 <= nx < len(a) and 0 <= ny < len(a) and (not (a[nx][ny] in dessert_list)):
                dessert_list.append(a[nx][ny])
                dir_list.append(next_dir)
                dfs(start_point,nx,ny,a,dir_list,dessert_list)
                dessert_list.pop()
                dir_list.pop()

for tc in range(1,testcase+1):
    n = int(input())
    a = [list(map(int,input().split())) for _ in range(n)]
    ans = 0

    for i in range(n):
        for j in range(n):
            if possible_start_point(i,j,a):
                dfs([i,j],i,j,a,[0],[])
    ans = ans if ans else -1
    print('#{} {}'.format(tc,ans))
