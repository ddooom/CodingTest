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
    ipt_list = []
    i,d = 0,0
    
    for _ in range(int(input())):
        
        act,n = input().split()
        
        if act == 'I':
            i += 1
            ipt_list.append(int(n))
            heapq.heappush(min_heap, int(n))
            heapq.heappush(max_heap, -int(n))
        
        if act == 'D':
            d += 1 
            print(i,d)
            if d > i: continue
            if n == '-1': 
                while 1:
                    pop = heapq.heappop(min_heap)
                    if pop in ipt_list:
                        ipt_list.remove(pop)
                        break

            else: 
                while 1:
                    pop = -heapq.heappop(max_heap)
                    if pop in ipt_list:
                        ipt_list.remove(pop)
                        break
                
    if d > i: print('EMPTY')
    else: print(-heapq.heappop(max_heap), heapq.heappop(min_heap))