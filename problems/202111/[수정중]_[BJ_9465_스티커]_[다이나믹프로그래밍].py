# BJ 9465 스티커 <다이나믹 프로그래밍>
# https://www.acmicpc.net/problem/9465
# 시간 : [경과 시간]
# 문제 리뷰 : [문제 리뷰]
# 회고 : [회고]


def dynamic(row, col, weight):
    if col < (n+1):
        return max(dynamic((row+1)%2, col+1, weight+F[row][col]),
                   dynamic((row+1)%2, col+2, weight+F[row][col]),
                   dynamic(row, col+2, weight+F[row][col]))
    else:
        return weight
    
    
T = int(input())
for _ in range(T):
    n = int(input())
    F = [[0]+list(map(int,input().split())) for _ in range(2)]
    print(max(dynamic(0, 0, 0), dynamic(1, 0, 0)))
