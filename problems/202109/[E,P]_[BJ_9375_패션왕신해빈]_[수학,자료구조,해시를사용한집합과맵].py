# BJ 9375 패션왕 신해빈 <수학, 자료 구조, 해시를 사용한 집합과 맵>
# https://www.acmicpc.net/problem/9375
# 시간 : 10
# 문제 리뷰 : E,P
# 회고 :


from collections import defaultdict

N=int(input())
for _ in range(N):
    d=defaultdict(list)
    for _ in range(int(input())):
        v,k=input().split()
        d[k].append(v)
    
    a = 1
    for v in map(len, d.values()):
        a *= v+1
    print(a-1)