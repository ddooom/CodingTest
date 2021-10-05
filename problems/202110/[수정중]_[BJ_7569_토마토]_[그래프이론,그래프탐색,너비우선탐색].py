# BJ 7569 토마토 <그래프 이론, 그래프 탐색, 너비 우선 탐색>
# https://www.acmicpc.net/problem/7569
# 시간 : 60
# 문제 리뷰 : H,R
# 회고 : 정답이랑 같은데 나만 틀린다..


import sys
print = sys.stdin.readline

M,N,H = map(int, input().split())

G = []
queue = []
for h in range(H):
    floor = []
    for n in range(N):
        row = list(map(int, input().split()))
        for m in range(M):
            if row[m] == 1:
                queue.append((m,n,h))
        floor.append(row)
    G.append(floor)


while queue:
    m,n,h = queue.pop(0)
    
    if m>0 and G[h][n][m-1] == 0: 
        queue.append((m-1,n,h))
        G[h][n][m-1] = G[h][n][m]+1
    if m<M-1 and G[h][n][m+1] == 0: 
        queue.append((m+1,n,h))
        G[h][n][m+1] = G[h][n][m]+1
    if n>0 and G[h][n-1][m] == 0: 
        queue.append((m,n-1,h))
        G[h][n-1][m] = G[h][n][m]+1
    if n<N-1 and G[h][n+1][m] == 0: 
        queue.append((m,n+1,h))
        G[h][n+1][m] = G[h][n][m]+1
    if h>0 and G[h-1][n][m] == 0: 
        queue.append((m,n,h-1))
        G[h-1][n][m] = G[h][n][m]+1
    if h<H-1 and G[h+1][n][m] == 0: 
        queue.append((m,n,h+1))
        G[h+1][n][m] = G[h][n][m]+1
        

day = 0
for f in G:
    for r in f:
        for t in r:
            if t == 0:
                print(-1)
                exit(0)
        day = max(day,max(r))
    
print(day-1)    