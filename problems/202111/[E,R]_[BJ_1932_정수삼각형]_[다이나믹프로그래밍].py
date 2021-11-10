# BJ 1932 정수 삼각형 <다이나믹 프로그래밍>
# https://www.acmicpc.net/problem/1932
# 시간 :15
# 문제 리뷰 : E, R
# 회고 : 


N = int(input())
T = [list(map(int, input().split())) for _ in range(N)]

for r in range(N-2, -1, -1):
    for i in range(r+1):
        T[r][i] = max(T[r][i]+T[r+1][i], T[r][i]+T[r+1][i+1])

print(T[0][0])