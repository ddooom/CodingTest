# BJ 9091 DSLR <그래프 이론, 그래프 탐색, 너비 우선 탐색>
# https://www.acmicpc.net/problem/9019
# 시간 : 40
# 문제 리뷰 : M,R
# 회고 : bfs를 진행할 때, pop하여 값을 받고 해당 값이 visit이 아니면 queue에 후보를 추가하는 것보다
#        queue에 후보를 추가할 때, visit을 체크하고 바로 visit[n] = 1을 해주는 것이 더 빨랐다.
#        또한, 해당 코드는 python3으로는 계속 시간 초과가 떠서 pypy3으로 제출하여 맞을 수 있었다.


from collections import deque

def bfs(A,B):
    queue = deque()
    queue.append([A, ''])
    visit = [0]*10000
    visit[A] = 1
    conditions = ['D', 'S', 'L', 'R']
    while 1:
        n,t = queue.popleft()

        values = [(n*2)%10000, 
                  9999 if n==0 else n-1,
                  (n%1000)*10 + n//1000,
                  (n%10)*1000 + n//10]
        
        for v, c in zip(values, conditions):
            if v==B:
                return t+c
            
            if not visit[v]:
                visit[v] = 1
                queue.append([v, t+c])
            

for _ in range(int(input())):
    A, B = map(int, input().split())
    print(bfs(A,B))