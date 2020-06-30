import sys
input = sys.stdin.readline

# 한 칸에 여러개의 나무를 심을 수도 있다.
# 가장 처음에 양분은 모든 칸에 5만큼
# 모든 칸에 대해서 조사를

# 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다
# 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다
# 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.

# 여름에는 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 소수점 아래는 버린다.

# 가을에는 나무가 번식한다. 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.

dx = [0,0,-1,1,-1,-1,1,1]
dy = [1,-1,0,0,1,-1,1,-1]

def spring():
    dead_tree=[]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if len(age_board[i][j]) > 0:
                candi = []
                for c in sorted(age_board[i][j]):
                    if yang_bun[i][j] >= c:
                        yang_bun[i][j]-=c
                        candi.append(c+1)
                    else:
                        dead_tree.append([i,j,c//2])
                age_board[i][j] = [x for x in candi]
    return dead_tree
def summer(dead_tree):
    for d in dead_tree:
        yang_bun[d[0]][d[1]] += d[2]
def fall():
    for i in range(1,n+1):
        for j in range(1,n+1):
            if len(age_board)>0:
                for c in age_board[i][j]:
                    if c%5==0:
                        for _ in range(8):
                            ni,nj = i+dx[_],j+dy[_]
                            if 1<=ni<=n and 1<=nj<=n:
                                age_board[ni][nj].append(1)
def winter():
    for i in range(1,n+1):
        for j in range(1,n+1):
            yang_bun[i][j]+=winter_y[i][j]

def one_year_later():
    summer(spring())
    fall()
    winter()

# nxn 들판 / m 개의 나무 심기 / k년후에 살아남은 나무의 수
n,m,k = map(int,input().split())
winter_y=[[0]*(n+1)]
for _ in range(n):
    tmp = list(map(int,input().split()))
    tmp.insert(0,0)
    winter_y.append(tmp)
yang_bun = [[5]*(n+1) for _ in range(n+1)]
age_board = [[[] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    i,j,age = map(int,input().split())
    age_board[i][j].append(age)


for _ in range(k):
    one_year_later()


ans = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        ans += len(age_board[i][j])
print(ans)