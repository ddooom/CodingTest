# BJ 2630 색종이 만들기 <분할 정복, 재귀>
# https://www.acmicpc.net/problem/2630
# 시간 : 15
# 문제 리뷰 : E, P
# 회고 : 재귀를 사용한 분할 정복

def check(n, p):
    s = sum(map(sum, p))
    if s == (n*n):
        return [0, 1]
    elif s == 0:
        return [1, 0]
    else:
        p1 = check(n//2, [p[i][:n//2] for i in range(0, n//2)])
        p2 = check(n//2, [p[i][:n//2] for i in range(n//2, n)])
        p3 = check(n//2, [p[i][n//2:] for i in range(0, n//2)])
        p4 = check(n//2, [p[i][n//2:] for i in range(n//2, n)])
        return [p1[0]+p2[0]+p3[0]+p4[0], p1[1]+p2[1]+p3[1]+p4[1]]

N = int(input())
p = [list(map(int, input().split())) for _ in range(N)]
a = check(N, p)
print(a[0])
print(a[1])