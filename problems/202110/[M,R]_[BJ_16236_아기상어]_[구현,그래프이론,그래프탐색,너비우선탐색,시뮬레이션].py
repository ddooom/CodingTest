# BJ 16236 아기 상어 <구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 시뮬레이션>
# https://www.acmicpc.net/problem/16236
# 시간 : 60
# 문제 리뷰 : M,R
# 회고 : bfs를 구현하고 이를 이용하여 구현을 하는 문제, 복잡하지만 어렵진 않은 문제


from collections import deque

def bfs(row, col):
    queue = deque()
    queue.append([row,col,0])
    visit = [[0]*N for _ in range(N)]
    
    eatable = []
    while queue:
        row,col,dist = queue.popleft()
        
        if not visit[row][col]:
            if 0<G[row][col]<SIZE:
                eatable.append([dist,row,col])
                
            visit[row][col] = 1
            
            if row>0 and G[row-1][col]<=SIZE: queue.append([row-1,col,dist+1])
            if row<(N-1) and G[row+1][col]<=SIZE: queue.append([row+1,col,dist+1])
            if col>0 and G[row][col-1]<=SIZE: queue.append([row,col-1,dist+1])
            if col<(N-1) and G[row][col+1]<=SIZE: queue.append([row,col+1,dist+1])
        
        
    return eatable


N = int(input())
G = []
MOVE = []
for r in range(N):
    row = list(map(int, input().split()))
    for c in range(N):
        if row[c] == 9:
            MOVE = [0,r,c]
    G.append(row)

SIZE = 2
EAT = 0
TIME = 0
while 1:
    row, col = MOVE[1], MOVE[2]
    G[row][col] = 0
    
    eatable = bfs(row,col)
    
    if len(eatable)==0:
        print(TIME)
        break
 
    MOVE = min(eatable, key=lambda x: (x[0],x[1],x[2]))
    
    TIME += MOVE[0]
    
    EAT += 1
    if EAT == SIZE:
        SIZE += 1
        EAT = 0