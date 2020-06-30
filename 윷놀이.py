import sys
input = sys.stdin.readline()

def move(cur,num):
    cur = node_dict[cur][1]
    for _ in range(num-1):
        cur = node_dict[cur][2]
    return cur

def dfs(idx,sum_score):
    global ans
    if idx < 10:
        for i in range(4):
            cur = h_idx[i]
            if cur != arrive_idx:
                nxt = move(cur,num_list[idx])
                if not (nxt in h_idx) or nxt==arrive_idx:
                    h_idx[i]=nxt
                    sum_score += node_dict[nxt][0]
                    dfs(idx+1,sum_score)
                    h_idx[i]=cur
                    sum_score -= node_dict[nxt][0]

    if ans < sum_score:
        ans = sum_score

node_dict = {}
h_idx=[0,0,0,0]
start_idx,arrive_idx=0,21
ans = 0
for i in range(22):
    if i==5:
        node_dict[i]=[i*2,22,i+1]
    elif i==10:
        node_dict[i]=[i*2,29,i+1]
    elif i==15:
        node_dict[i]=[i*2,28,i+1]
    elif i==21:
        node_dict[i]=[0,i,i]
    else:
        node_dict[i]=[i*2,i+1,i+1]

node_dict[22],node_dict[23],node_dict[24],node_dict[25],\
node_dict[26],node_dict[27],node_dict[28],node_dict[29],\
node_dict[30],node_dict[31],node_dict[32]=\
[13,23,23],[16,24,24],[19,25,25],[25,31,31],\
[26,25,25],[27,26,26],[28,27,27],[22,30,30],\
[24,25,25],[30,32,32],[35,20,20]

num_list=list(map(int,input.split()))
dfs(0,0)
print(ans)