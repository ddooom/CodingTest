# BJ 16953 A → B <그래프 이론, 그리디 알고리즘, 그래프 탐색, 너비 우선 탐색>
# https://www.acmicpc.net/problem/16953
# 시간 : 15
# 문제 리뷰 : E,P
# 회고 : 


from collections import deque

def bfs():
    queue = deque([[A, 1]])
    while queue:
        a, n = queue.popleft()
        
        if 2*a == B or 10*a+1 == B:
            return n + 1
        
        if 2*a < B:
            queue.append([2*a, n+1])
        if 10*a+1 < B:
            queue.append([10*a+1, n+1])
    
    return -1        


A, B = map(int, input().split())
if A==B:
    print(1)
else:
    print(bfs())