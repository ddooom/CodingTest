# BJ 11725 트리의 부모 찾기 <그래프 이론, 그래프 탐색, 트리, 너비 우선 탐색, 깊이 우선 탐색>
# https://www.acmicpc.net/problem/11725
# 시간 : 20
# 문제 리뷰 : E,R
# 회고 : 


from collections import defaultdict, deque
import sys

input = sys.stdin.readline

N = int(input())
G = defaultdict(list)
for _ in range(N-1):
    n1,n2 = map(int,input().split())
    G[n1].append(n2)
    G[n2].append(n1)

parent = [0] * (N+1)
visit = [0] * (N+1)
queue = deque([1])

while queue:
    n = queue.popleft()
    
    if not visit[n]:
        visit[n] = 1
        
        for i in G[n]:
            queue.append(i)
            if not parent[i]:
                parent[i] = n
                
print('\n'.join(map(str,parent[2:])))