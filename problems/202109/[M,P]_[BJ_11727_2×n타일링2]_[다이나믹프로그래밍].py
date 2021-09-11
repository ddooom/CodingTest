# BJ 11727 2×n 타일링2 <다이나믹 프로그래밍>
# https://www.acmicpc.net/problem/11727
# 시간 : 15
# 문제 리뷰 : M,P
# 회고 : 2×n 타일링과 비슷한 문제

a,b,n=1,3,int(input())
if n==1: print(a)
elif n==2: print(b)
else:
    for _ in range(n-2):
        a,b=b,2*a+b
    print(b%10007)