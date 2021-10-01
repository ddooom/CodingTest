# BJ 2178 미로 탐색 <그래프 이론, 그래프 탐색, 너비 우선 탐색>
# https://www.acmicpc.net/problem/2178
# 시간 : 20
# 문제 리뷰 : M,P
# 회고 : 본인 코드는 2차원 배열을 연결 리스트 형식의 그래프로 바꾼 뒤 bfs를 진행하였다.
#        하지만 Faster Code는 2차원 배열 그대로에서 bfs 형식으로 진행하였다. 또한 check을 따로 만들지 않고 지나갔으면 해당 위치를 0으로 바꾸어 해결하였다.


N,M = map(int,input().split())
F = [list(input()) for _ in range(N)]

G = []
for r in range(N):
    for c in range(M):
        if F[r][c] == '0': G.append([])
        else:
            p = []
            if c>0 and F[r][c-1]=='1': p.append(M*r+c-1)
            if c<M-1 and F[r][c+1]=='1': p.append(M*r+c+1)
            if r>0 and F[r-1][c]=='1': p.append(M*r+c-M)
            if r<N-1 and F[r+1][c]=='1': p.append(M*r+c+M)
            G.append(p)
            
queue = [(n, 2) for n in G[0]]
check = [0]*M*N
check[0] = 1
while queue:
    n, cnt = queue.pop(0)
    
    if n == M*N-1:
        print(cnt)
        break
    
    if check[n] == 0:
        check[n] = 1
        queue.extend([(n, cnt+1) for n in G[n]])


''' Faster Code
from sys import stdin

n,m = map(int,input().split())

maze = [[0]*(m+2)]
for _ in range(n):
    maze.append([0]+list(map(int,list(stdin.readline().rstrip("\n"))))+[0])
maze.append([0]*(m+2))

que = [(1,1)]
maze[1][1] == 0
count = 1
while True:
    temp = []
    for node in que:
        i,j = node
        if maze[i+1][j] != 0:
            temp.append((i+1,j))
            maze[i+1][j] = 0

        if maze[i-1][j] != 0:
            temp.append((i-1,j))
            maze[i-1][j] = 0

        if maze[i][j+1] != 0:
            temp.append((i,j+1))
            maze[i][j+1] = 0

        if maze[i][j-1] != 0:
            temp.append((i,j-1))
            maze[i][j-1] = 0


    que = temp
    count += 1
    if (n,m) in temp:
        break

print(count)
'''