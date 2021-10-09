# BJ 2667 단지번호붙이기 <그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색>
# https://www.acmicpc.net/problem/2667
# 시간 : 20
# 문제 리뷰 : M,P
# 회고 : 

N = int(input())
G = [list(map(int, input())) for _ in range(N)]

queue = []
n = 0
h_list = []
h = 0

while 1:
    if not queue:
        for i in range(N):
            if 1 in G[i]:
                n += 1
                h_list.append(h)
                h = 0
                queue.append((i, G[i].index(1)))
                break
    
    if not queue: h_list.append(h); break
    r,c = queue.pop(0)
    
    if G[r][c]:
        h += 1
        G[r][c] = 0
        
        if r>0 and G[r-1][c]: queue.append((r-1, c))
        if r<N-1 and G[r+1][c]: queue.append((r+1, c))
        if c>0 and G[r][c-1]: queue.append((r, c-1))
        if c<N-1 and G[r][c+1]: queue.append((r, c+1))
    
print(n)
print('\n'.join(map(str,sorted(h_list[1:]))))