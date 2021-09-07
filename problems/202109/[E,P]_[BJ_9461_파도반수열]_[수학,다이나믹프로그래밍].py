# BJ 9461 파도반 수열 <수학, 다이나믹 프로그래밍>
# https://www.acmicpc.net/problem/9461
# 시간 : 10
# 문제 리뷰 : E,P
# 회고 : 


p=[1,1,1,2,2]
for i in range(95):
    p.append(p[-1]+p[i])

for _ in range(int(input())):
    print(p[int(input())-1])