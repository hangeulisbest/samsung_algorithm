import sys
sys.stdin = open("input.txt","r")

dx = [0,0,-1,1]
dy = [1,-1,0,0]
testCase = int(input())

def move(atom,ans):
    d = {}
    delList=[]
    for i in range(len(atom)):
        tx = atom[i][0] + dx[atom[i][2]]
        ty = atom[i][1] + dy[atom[i][2]]
        if abs(tx)>2000 or abs(ty)>2000:
            delList.append(i)
        else:
            string = '{} {}'.format(tx,ty)
            if string in d:
                d[string].append(i)
            else:
                d[string]=[]
                d[string].append(i)
        atom[i][0]=tx
        atom[i][1]=ty

    for idx,val in d.items():
        if len(val) > 1:
            for v in val:
                ans += atom[v][3]
                delList.append(v)

    tmp=[]
    for i in range(len(atom)):
        if not( i in delList):
            tmp.append(atom[i])

    return tmp,ans

for tc in range(1,testCase+1):
    n = int(input())
    atom=[]
    ans =0
    for _ in range(n):
        a,b,dir,energy = map(int,input().split())
        atom.append([2*a,2*b,dir,energy])

    while len(atom)>0:
        atom,ans = move(atom,ans)
    print("#{} {}".format(tc,ans))

