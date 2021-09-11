# BJ 11726 2×n 타일링 <다이나믹 프로그래밍>
# https://www.acmicpc.net/problem/11726
# 시간 : 20
# 문제 리뷰 : M, P
# 회고 : 다이나믹 프로그래밍의 기초


a,b,n=1,2,int(input())
if n<3: print(n)
else:
    for _ in range(n-2):
        a,b=b,a+b
    print(b%10007)