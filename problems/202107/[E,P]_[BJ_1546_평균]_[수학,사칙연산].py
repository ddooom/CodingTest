# BJ 1546 평균 <수학, 사칙연산>
# https://www.acmicpc.net/problem/1546
# 시간 : 5
# 문제 리뷰 : E, P
# 회고 : 

n, data = int(input()), list(map(int, input().split()))
m = max(data)
print(sum(map(lambda x: x/m*100, data))/n)
