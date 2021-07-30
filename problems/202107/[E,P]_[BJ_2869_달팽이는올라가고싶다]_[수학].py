# BJ 2869 달팽이는 올라가고 싶다 <수학>
# https://www.acmicpc.net/problem/2869
# 시간 : 10
# 문제 리뷰 : E, P
# 회고 : 


a, b, v = map(int, input().split())
print(-int(-((v-a)/(a-b))//1)+1)