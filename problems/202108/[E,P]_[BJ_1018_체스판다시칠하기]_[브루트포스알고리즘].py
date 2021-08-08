# BJ 1018 체스판 다시 칠하기 <브루트포스 알고리즘>
# https://www.acmicpc.net/problem/1018
# 시간 : 15
# 문제 리뷰 : E,P
# 회고 : 


w,b='WBWBWBWB','BWBWBWBW'
c1,c2=[w,b,w,b,w,b,w,b],[b,w,b,w,b,w,b,w]

m,n=map(int,input().split())
l=[input() for _ in range(m)]

result = []
for r in range(m-7):
    for c in range(n-7):
        result.append(sum([l[i+r][j+c]==c1[i][j] for i in range(8) for j in range(8)]))
        result.append(sum([l[i+r][j+c]==c2[i][j] for i in range(8) for j in range(8)]))

print(min(result))