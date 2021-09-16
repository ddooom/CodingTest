# BJ 1780 종이의 개수 <분할 정복, 재귀>
# https://www.acmicpc.net/problem/1780
# 시간 : 60
# 문제 리뷰 : H,R
# 회고 : 재귀함수에서 공통의 값을 누적해야할 땐, return으로 쌓기보단 global로 전역 변수화하여 구현하는 것이 편리하다.
#        또한 분할 정복을 할 때, 배열을 인덱싱하여 입력하는 것보단, 배열을 전역으로하여 인덱싱할 인덱스를 입력하는 것이 더 빨랐다.


def check(row, col, dim):
    global minus, zero, plus
    
    next_dim = dim//3
    n = paper[row][col]
    for r in range(row, row+dim):
        for c in range(col, col+dim):
            if paper[r][c] != n:
                check(row, col, next_dim)
                check(row, col+next_dim, next_dim)
                check(row, col+2*next_dim, next_dim)
                check(row+next_dim, col, next_dim)
                check(row+next_dim, col+next_dim, next_dim)
                check(row+next_dim, col+2*next_dim, next_dim)
                check(row+2*next_dim, col, next_dim)
                check(row+2*next_dim, col+next_dim, next_dim)
                check(row+2*next_dim, col+2*next_dim, next_dim)
                return 
    
    if n == -1: minus += 1
    elif n == 0: zero += 1
    elif n == 1: plus += 1
    
    return
    
dim = int(input())
paper = [list(map(int, input().split())) for _ in range(dim)]
minus, zero, plus = 0, 0, 0
check(0,0,dim)
print(minus)
print(zero)
print(plus)