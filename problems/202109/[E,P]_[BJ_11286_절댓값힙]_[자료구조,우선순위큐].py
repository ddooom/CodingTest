# BJ 11286 절댓값 힙 <자료 구조, 우선순위 큐>
# https://www.acmicpc.net/problem/11286
# 시간 : 15
# 문제 리뷰 : E,P
# 회고 : 


import heapq
import sys

input = sys.stdin.readline

h = []
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if len(h) == 0: print(0)
        else: print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (abs(n), n))