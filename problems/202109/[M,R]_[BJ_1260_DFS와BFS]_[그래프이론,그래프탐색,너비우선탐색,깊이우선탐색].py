# BJ 1260 DFS와 BFS <그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색>
# https://www.acmicpc.net/problem/1260
# 시간 : 30
# 문제 리뷰 : M, R
# 회고 : DFS와 BFS의 기본적인 구현 문제, 비재귀 형식으로 구현하였으며 그래프는 딕셔너리를 이용한 연결 리스트로 구현하였다.
#        Faster Code는 리스트의 인덱스를 이용하여 연결 리스트를 구현하였으며 방문한 노드는 1로 표시하는 리스트를 따로 만들어 효율적인 코드를 구현하였다.


def dfs(l, n):
    v, s = [], [n]
    while len(s) > 0:
        n = s.pop(-1)

        if n not in v:
            if n in l.keys():
                s.extend(sorted(l[n], reverse=True))
                del l[n]
            v.append(n)
            
    return ' '.join(map(str,v))

def bfs(l, n):
    v, s = [], [n]
    while len(s) > 0:
        n = s.pop(0)

        if n not in v:
            if n in l.keys():
                s.extend(sorted(l[n]))
                del l[n]
            v.append(n)
            
    return ' '.join(map(str,v))

from collections import defaultdict

N, M, V = map(int, input().split())
L = defaultdict(list)
for _ in range(M):
    h,t = map(int, input().split())
    L[h].append(t)
    L[t].append(h)

print(dfs(L.copy(), V))
print(bfs(L.copy(), V))


''' Faster Code
import sys
N, M, V = map(int, sys.stdin.readline().strip().split())
edge = [[] for _ in range(N+1)]

for __ in range(M):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    edge[n1].append(n2)
    edge[n2].append(n1)

for e in edge:
    e.sort(reverse=True)

def dfs():
    d_visit = []
    stack = [V]
    d_check = [0 for _ in range(N+1)]
    while stack:
        v1 = stack.pop()
        if not d_check[v1]:
            d_check[v1] = 1
            d_visit.append(v1)
            stack += edge[v1]
    return d_visit


def bfs():
    b_visit = []
    queue = [V]
    b_check = [0 for _ in range(N+1)]
    b_check[V] = 1
    while queue:
        v2 = queue.pop()
        b_visit.append(v2)
        for i in reversed(edge[v2]):
            if not b_check[i]:
                b_check[i] = 1
                queue = [i] + queue
    return b_visit

print(' '.join(map(str,dfs())))
print(' '.join(map(str,bfs())))
'''