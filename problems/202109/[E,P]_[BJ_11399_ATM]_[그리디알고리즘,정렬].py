# BJ 11399 ATM <그리디 알고리즘, 정렬>
# https://www.acmicpc.net/problem/11399
# 시간 : 10
# 문제 리뷰 : E,P
# 회고 : 


n=int(input())
t=sorted(list(map(int, input().split())))
print(sum([t[i]*(n-i) for i in range(n)]))