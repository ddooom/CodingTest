# BJ 11279 최대 힙 <자료 구조, 우선순위 큐>
# https://www.acmicpc.net/problem/11279
# 시간 : 20
# 문제 리뷰 : M,R
# 회고 : 파이썬의 heapq 라이브러리를 사용한 방법과 heap을 클래스로 구현한 방법을 모두 사용해보았다.


import heapq
import sys
input = sys.stdin.readline
heap = []
for _ in range(int(input())):
    n = int(input())
    if n==0:
        if len(heap)==0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    
    else:
        heapq.heappush(heap, -n)


''' Heap using Class
import sys
input = sys.stdin.readline

class heap:
    def __init__(self):
        self.heap = [0]
        self.len = 0
    
    def __len__(self):
        return self.len
    
    def push(self, n):
        self.heap.append(n)
        self.len += 1
        i = self.len
        
        while (i!=1) and (n>self.heap[i//2]):
            self.heap[i//2],self.heap[i] = self.heap[i],self.heap[i//2]
            i = i//2
    
    def pop(self):
        if self.len == 0:
            return self.heap[0]
        if self.len == 1:
            self.len -= 1
            return self.heap.pop()
        
        t = self.heap[1]
        self.len -= 1
        self.heap[1] = self.heap.pop()
        parent = 1
        child = 2
        
        while child <= self.len:
            if (child<self.len) and (self.heap[child]<self.heap[child+1]):
                child += 1
            
            if self.heap[parent] > self.heap[child]:
                break
            
            self.heap[parent],self.heap[child] = self.heap[child],self.heap[parent]
            parent = child
            child *= 2
        
        return t
    

h = heap()
for _ in range(int(input())):
    n = int(input())
    if n==0:
        print(h.pop())
    else:
        h.push(n)
'''