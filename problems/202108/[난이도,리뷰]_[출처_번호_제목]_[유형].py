# BJ 2606 바이러스 <그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색>
# https://www.acmicpc.net/problem/2606
# 시간 : [경과 시간]
# 문제 리뷰 : [문제 리뷰]
# 회고 : [회고]


from collections import defaultdict
import sys
input = sys.stdin.readline

# R,N=int(input()),int(input())
# g=defaultdict(list)
# for _ in range(N):
#     a,b=map(int, input().split())
#     g[a].append(b)

# v=set()
# s=g[1]
# while len(s)!=0:
#     v.add(s[0])
#     s.extend(g[s.pop(0)])
# print(len(v))


R,N=input(),int(input())
g=[]
for _ in range(N):
    a,b=map(int, input().split())
    c = 0
    for i in range(len(g)):
        if a in g[i]: 
            g.append(g.pop(i)+[a,b]) 
            c+=1
        if b in g[i]: 
            g.append(g.pop(i)+[a,b]); 
            c+=1
    if c==0: g.append([a,b])
    
for s in g:
    if 1 in s:
        print(len(set(s))-1)
        break