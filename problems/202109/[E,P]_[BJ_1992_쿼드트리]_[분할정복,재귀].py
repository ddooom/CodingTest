# BJ 1992 쿼드트리 <분할 정복, 재귀>
# https://www.acmicpc.net/problem/1992
# 시간 : 15
# 문제 리뷰 : E,P
# 회고 :


def solution(r, c, d):
    if sum([sum(F[i][c:c+d]) for i in range(r,r+d)])==0:
        return str(0)
    elif all([all(F[i][c:c+d]) for i in range(r,r+d)]):
        return str(1)
    
    else:
        return '(' + solution(r,c,d//2) + solution(r,c+d//2,d//2) + solution(r+d//2,c,d//2) + solution(r+d//2,c+d//2,d//2) + ')'

N = int(input())
F = [list(map(int, input())) for _ in range(N)]

print(solution(0,0,N))