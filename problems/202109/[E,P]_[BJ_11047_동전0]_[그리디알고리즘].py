# BJ 11047 동전 0 <그리디 알고리즘>
# https://www.acmicpc.net/problem/11047
# 시간 : 15
# 문제 리뷰 : E,P
# 회고 : 


N,T=map(int, input().split())
l=[int(input()) for _ in range(N)]
a=0
for i in range(N-1,-1,-1):
    if l[i] <= T:
        n=(T//l[i])
        T-=l[i]*n
        a+=n
        if T==0:
            print(a)
            break