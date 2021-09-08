# BJ 11659 구간 합 구하기 4 <누적 합>
# https://www.acmicpc.net/problem/11659
# 시간 : 20
# 문제 리뷰 : E,R
# 회고 : 시간 효율이 중요한 문제로 단순 인덱싱으로 하여 sum()을 하면 시간 초과이다.
#        따라서 구간 누적 합을 구한 뒤, 해당 범위의 합을 구해야 한다.


import sys
input=sys.stdin.readline

N,M=map(int,input().split())
l=list(map(int,input().split()))
c=[0]
for i in range(N):
    c.append(l[i]+c[-1])

for _ in range(M):
    a,b=map(int,input().split())
    print(c[b]-c[a-1])