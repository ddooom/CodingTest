# BJ 1697 숨바꼭질 <그래프 이론, 그래프 탐색, 너비 우선 탐색>
# https://www.acmicpc.net/problem/1697
# 시간 : 30
# 문제 리뷰 : M,R
# 회고 : 본인은 bfs로 풀이하였다. Faster Code를 보면 n의 입장이 아닌 k의 입장에서 풀이하였다.


N,K = map(int, input().split())
queue = [(N,0)]
visit = [0]*200000

while queue:
    n,cnt = queue.pop(0)
    
    if n == K:print(cnt);break
    
    if not visit[n] and n>=0:
        visit[n] = 1

        if n > K:
            queue.append((n-1, cnt+1))
        else: 
            queue.append((n-1, cnt+1))
            queue.append((n+1, cnt+1))
            queue.append((2*n, cnt+1))


''' Faster Code
def find(n, k):
    if n >= k:
        return n-k
    elif k == 1:
        return 1
    elif k%2:
        return min(find(n, k-1), find(n, k+1)) + 1
    else:
        return min(k-n, find(n, k//2) + 1)
  
import sys
n, k = map(int, sys.stdin.readline().split())
print(find(n, k))
'''