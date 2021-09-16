# BJ 11724 연결 요소의 개수 <그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색>
# https://www.acmicpc.net/problem/11724
# 시간 : 20
# 문제 리뷰 : M, R
# 회고 : 본인의 코드는 연결 리스트로 그래프를 나타내었고 dfs를 진행하였다.
#        Other Code는 인접행렬로 리스트를 나타내었고 bfs를 진행하였다. 또한 bfs를 함수로 하여 check가 0일 때 해당 노드에서 bfs가 시작하게 하였다.


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    G[n1].append(n2)
    G[n2].append(n1)
    
cc = 1
stack = G[1].copy()
check = [0] * (N+1)
check[1] = 1

while sum(check) != N:
    
    if len(stack)==0:
        cc += 1
        n = check[1:].index(0)+1
        stack.extend(G[n])
        check[n] = 1
    
    else:
        n = stack.pop(0)
        if not check[n]:
            check[n] = 1
            stack.extend(G[n])

print(cc)


''' Other Code
import sys

def bfs(v) :
    queue = [v]
    check[v] = 1
    while queue :
        v = queue.pop(0)
        for i in range(1, n+1) :
            if check[i] == 0 and graph[v][i] == 1 :
                queue.append(i)
                check[i] = 1

n, m = map(int,sys.stdin.readline().split())

graph = [[0]*(n+1) for i in range(n+1)]
check = [0 for i in range(n+1)]

for i in range(m) :
    x,y  = map(int,sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

cnt = 0

for i in range(1,n+1) :
    if check[i] == 0 :
        bfs(i)
        cnt+=1

sys.stdout.write(str(cnt)+'\n')

'''