# BJ 1389 케빈베이컨의6단계법칙 <그래프 이론, 그래프 탐색, 너비 우선 탐색, 플로이드-와샬>
# https://www.acmicpc.net/problem/1389
# 시간 : 20
# 문제 리뷰 : E,P
# 회고 : 


def bfs(target):
    queue = [target]
    visit = [0]*(N+1)
    visit[target] = 1

    while queue:
        n = queue.pop(0)

        for i in G[n]:
            if not visit[i]:
                visit[i] = visit[n]+1
                queue.append(i)
    
    return sum(visit)-N

N, M = map(int, input().split())
G = {i : [] for i in range(1,N+1)}
for _ in range(M):
    n1, n2 = map(int, input().split())
    G[n1].append(n2)
    G[n2].append(n1)
    
far = []
for i in range(1, N+1):
    far.append(bfs(i))

print(far.index(min(far))+1)