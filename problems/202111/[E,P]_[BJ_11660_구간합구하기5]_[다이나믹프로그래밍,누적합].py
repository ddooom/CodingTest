# BJ 11660 구간 합 구하기 5 <다이나믹 프로그래밍, 누적 합>
# https://www.acmicpc.net/problem/11660
# 시간 : 15
# 문제 리뷰 : E, P
# 회고 : 이전에 경험해본 유형


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
F = [[0 for _ in range(N+1)] for _ in range(N+1)]

for row_idx in range(1,N+1):
    row = list(map(int, input().split()))
    for col_idx in range(1,N+1):
        F[row_idx][col_idx] = F[row_idx][col_idx-1] + F[row_idx-1][col_idx] - F[row_idx-1][col_idx-1] + row[col_idx-1] 
        
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(F[x2][y2] - F[x2][y1-1] - F[x1-1][y2] + F[x1-1][y1-1])