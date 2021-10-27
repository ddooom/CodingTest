# BJ 7662 이중 우선순위 큐 <자료 구조, 트리를 사용한 집합과 맵, 우선순위 큐>
# https://www.acmicpc.net/problem/7662
# 시간 : [경과 시간]
# 문제 리뷰 : [문제 리뷰]
# 회고 : [회고]


import heapq
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    
    min_heap = []
    max_heap = []
    visit = [0] * 5000000
    
    for _ in range(int(input())):
        
        act,n = input().split()
        
        if act == 'I':
            visit[int(n)] += 1
            heapq.heappush(min_heap, int(n))
            heapq.heappush(max_heap, -int(n))
        
        elif act == 'D':

            if n == '-1': 
                while 1:
                    if not min_heap:
                        break
                    pop = heapq.heappop(min_heap)
                    if visit[pop]:
                        visit[pop] -= 1
                        break

            else: 
                while 1:
                    if not max_heap:
                        break
                    pop = -heapq.heappop(max_heap)
                    if visit[pop]:
                        visit[pop] -= 1
                        break
    
    result = []
    
    while 1:
        if not min_heap:
            break
        pop = heapq.heappop(min_heap)
        if visit[pop]:
            visit[pop] -= 1
            result.append(pop)
            break
                        
    while 1:
        if not max_heap:
            break
        pop = -heapq.heappop(max_heap)
        if visit[pop]:
            visit[pop] -= 1
            result.append(pop)
            break

    if result: print(result[-1], result[0])
    else: print('EMPTY')