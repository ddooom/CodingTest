# BJ 10026 백록색약 <그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색>
# https://www.acmicpc.net/problem/10026
# 시간 : 30
# 문제 리뷰 : M, P
# 회고 : 그래프로 풀수 있지만 Other Answer처럼 그리디하게도 해결할 수 있다. 그리디 알고리즘이 더 효율적


def bfs(G):
    queue = [0]
    check = [0]*N*N
    sub = 1
    
    while 1:
        if all(check):
            break
        
        if not queue: 
            queue.append(check.index(0))
            sub += 1
        
        n = queue.pop()
        c = G[n//N][n%N]
        if not check[n]:
            check[n] = 1
            
            if n//N>0 and G[n//N-1][n%N]==c: queue.append(n-N)
            if n//N<N-1 and G[n//N+1][n%N]==c: queue.append(n+N)
            if n%N>0 and G[n//N][n%N-1]==c: queue.append(n-1)
            if n%N<N-1 and G[n//N][n%N+1]==c: queue.append(n+1)
    
    return sub


N = int(input())
G1 = [input() for _ in range(N)]
G2 = [s.replace('G', 'R') for s in G1]
print(bfs(G1), bfs(G2))


''' Other Answer
import sys
sys.setrecursionlimit(10**5)
n=int(input())
a=[[" "]*(n+2)]+[list(" "+input()+" ")for i in[0]*n]+[[" "]*(n+2)]
b=[i.copy()for i in a]
def cnt(s,x,y,c):
    s[x][y]=" "
    if s[x-1][y]==c:cnt(s,x-1,y,c)
    if s[x+1][y]==c:cnt(s,x+1,y,c)
    if s[x][y-1]==c:cnt(s,x,y-1,c)
    if s[x][y+1]==c:cnt(s,x,y+1,c)
c=d=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if a[i][j]!=" ":
            cnt(a,i,j,a[i][j]);c+=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if b[i][j]=="G":b[i][j]="R"
for i in range(1,n+1):
    for j in range(1,n+1):
        if b[i][j]!=" ":
            cnt(b,i,j,b[i][j]);d+=1
print(c,d)
'''