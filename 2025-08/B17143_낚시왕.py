import sys
input = sys.stdin.readline

r,c,m = map(int, input().split())
board=[[[]for _ in range(c)]for _ in range(r)]

for _ in range(m):
    x,y,s,d,z=map(int, input().split())
    board[x-1][y-1].append([s,d-1,z])

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def catch(y,board):
    ans=0
    for i in range(r):
        if board[i][y]:
            ans=board[i][y][0][2]
            board[i][y]=[]
            break
    return ans,board

def move(board):
    tmp=[[[]for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j]:
                x,y=i,j
                s,d,z=board[i][j][0]
                distance=s
                while distance:
                    x,y=x+dx[d], y+dy[d]
                    if 0<=x<r and 0<=y<c:
                        distance=1
                    else:
                        x,y=x-dx[d], y-dy[d]
                        if d==0: d=1
                        elif d==1: d=0
                        elif d==2: d=3
                        elif d==3: d=2
                tmp[x][y].append([s,d,z])

    for i in range(r):
        for j in range(c):
            if len(tmp[i][j])>=2:
                tmp[i][j].sort(key=lambda x:x[2], reverse=True)
                s,d,z=tmp[i][j][0]
                tmp[i][j]=[[s,d,z]]
    return tmp

shark=0
for i in range(c):
    eat,board=catch(i,board)
    shark+=eat
    board=move(board)

print(shark)