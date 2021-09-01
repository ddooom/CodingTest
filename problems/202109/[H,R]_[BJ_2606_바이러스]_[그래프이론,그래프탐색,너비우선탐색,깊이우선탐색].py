# BJ 2606 바이러스 <그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색>
# https://www.acmicpc.net/problem/2606
# 시간 : 40
# 문제 리뷰 : H, R
# 회고 : defaultdict을 이용하여 그래프를 구현하였고 bfs를 통하여 1과 연결된 노드 수를 구하였다.
#        Best Answer은 리스트를 활용하여 그래프를 구현하였고 heap을 이용하여 dfs를 구현하였다.


from collections import defaultdict
import sys
input = sys.stdin.readline

R,N=int(input()),int(input())
g=defaultdict(list)
for _ in range(N):
    a,b=map(int, input().split())
    g[a].append(b)
    g[b].append(a)

v=set()
s=g[1]
while len(s)!=0:
    n = s.pop(0)
    if n in v: continue 
    v.add(n)
    s.extend(g[n])
print(len(v)-1)


''' Best Answer
import sys

def dfs(n):
    Heap.append(n)
    for v in V[n]:
        if v not in Heap:
            dfs(v)


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

V = [[] for _ in range(N + 1)]
Heap = []

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    V[a].append(b)
    V[b].append(a)

dfs(1)

print(len(Heap) - 1)
'''