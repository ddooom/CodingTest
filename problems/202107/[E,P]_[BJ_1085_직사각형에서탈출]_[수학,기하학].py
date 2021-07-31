# BJ 1085 직사각형에서 탈출 <수학, 기하학>
# https://www.acmicpc.net/problem/1085
# 시간 : 5
# 문제 리뷰 : E, P
# 회고 : 

x, y, w, h = map(int, input().split())
print(min([w-x, h-y, x, y]))