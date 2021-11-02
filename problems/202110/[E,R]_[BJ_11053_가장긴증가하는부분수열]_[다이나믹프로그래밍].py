# BJ 11053 가장 긴 증가하는 부분 수열 <다이나믹 프로그래밍>
# https://www.acmicpc.net/problem/11053
# 시간 :15
# 문제 리뷰 : E, R
# 회고 : 


N = int(input())
T = [list(map(int, input().split())) for _ in range(N)]

for r in range(N-2, -1, -1):
    for i in range(r+1):
        T[r][i] = max(T[r][i]+T[r+1][i], T[r][i]+T[r+1][i+1])

print(T[0][0])