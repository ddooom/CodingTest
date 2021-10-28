# BJ 7662 이중 우선순위 큐 <자료 구조, 트리를 사용한 집합과 맵, 우선순위 큐>
# https://www.acmicpc.net/problem/7662
# 시간 : 60+
# 문제 리뷰 : H,R
# 회고 : 첫 문제 풀이는 visit을 입력 받은 수의 개수의 리스트로 정의하여 인덱스 에러가 발생하였다.
#        이유는 입력 값의 범위는 정해져 있지 않았기 때문에 32비트의 수를 처리하여야 했으나 2**32 길이의 리스트는 메모리 초과이기 때문이다.
#        따라서 들어오는 순서를 i로 하여 i의 visit 여부로 visit 을 정의하여 해결하였다.


import heapq
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    
    min_heap = []
    max_heap = []
    visit = [0] * 1000000
    
    for i in range(int(input())):
        
        act,n = input().split()
        
        if act == 'I':
            visit[i] = 1
            heapq.heappush(min_heap, (int(n),i))
            heapq.heappush(max_heap, (-int(n),i))
        
        elif act == 'D':

            if n == '-1': 
                while 1:
                    if not min_heap:
                        break
                    pop,idx = heapq.heappop(min_heap)
                    if visit[idx]:
                        visit[idx] = 0
                        break

            else: 
                while 1:
                    if not max_heap:
                        break
                    pop,idx = heapq.heappop(max_heap)
                    if visit[idx]:
                        visit[idx] = 0
                        break
    
    result = []
    
    while 1:
        if not min_heap:
            break
        pop,idx = heapq.heappop(min_heap)
        if visit[idx]:
            visit[idx] = 0
            result.append(pop)
            break
                        
    while 1:
        if not max_heap:
            break
        pop,idx = heapq.heappop(max_heap)
        if visit[idx]:
            visit[idx] = 0
            result.append(-pop)
            break

    if result: print(result[-1], result[0])
    else: print('EMPTY')