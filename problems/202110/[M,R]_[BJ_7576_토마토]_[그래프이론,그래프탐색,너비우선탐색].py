# BJ 7576 토마토 <그래프 이론, 그래프 탐색, 너비 우선 탐색>
# https://www.acmicpc.net/problem/7576
# 시간 : 30
# 문제 리뷰 : M,R
# 회고 : 이전에는 bfs를 진행할 때, list.pop(0)을 진행하였다. 하지만 pop연산을 진행할 때 0번째를 pop하는 것의 시간 복잡도는 O(n) 이라고 한다.
#        따라서 deque를 사용하여 popleft()를 해줘야 했었다.


from collections import deque

M,N = map(int, input().split())
G = []
queue = deque([])

for r in range(N):
    row = list(map(int, input().split()))
    for c in range(M):
        if row[c]==1: queue.append((r,c))
    G.append(row)

m = 0
while queue:
    r, c = queue.popleft()

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    for x, y in zip(dx, dy):
        if 0<=r+x<N and 0<=c+y<M and not G[r+x][c+y]:
            queue.append((r+x, c+y))
            G[r+x][c+y] = G[r][c] + 1
            m = max(m, G[r][c] + 1)
            
fail = False
for r in G:
    for c in r:
        if not c:
            print(-1)
            fail = True
            break

if not fail:
    print(m-1)