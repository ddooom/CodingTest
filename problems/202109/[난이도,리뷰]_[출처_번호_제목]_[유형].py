# BJ 16928 뱀과 사다리 게임 <그래프 이론, 그래프 탐색, 너비 우선 탐색>
# https://www.acmicpc.net/problem/16928
# 시간 : [경과 시간]
# 문제 리뷰 : [문제 리뷰]
# 회고 : [회고]


import sys
input = sys.stdin.readline

P = {}
for _ in range(sum(map(int, input().split()))):
    a, b = (map(int, input().split()))
    P[a] = b

queue = [(i,1) for i in range(2,8)]
check = [0] * 101
check[1] = 1
while len(queue) != 0:
    n, cnt = queue.pop(0)
    if check[n] == 0:
        
        check[n] = 1
        queue.extend([(n+i,cnt+1) for i in range(1,7)])
        
        if n in P.keys():
            queue.append((P[n], cnt))
        
        if n==100:
            print(cnt)
            break