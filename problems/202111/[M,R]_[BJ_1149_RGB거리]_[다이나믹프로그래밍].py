# BJ 1149 RGB거리 <다이나믹프로그래밍>
# https://www.acmicpc.net/problem/1149
# 시간 : 15
# 문제 리뷰 : M,R
# 회고 : BJ 9465 스티커와 해결 방법이 같은 문제로, 스티커를 푼 뒤 해결하여 어렵지 않았다.


N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    F[i][0] += min(F[i-1][1], F[i-1][2])
    F[i][1] += min(F[i-1][0], F[i-1][2])
    F[i][2] += min(F[i-1][0], F[i-1][1])
    
print(min(F[-1][0], F[-1][1], F[-1][2]))