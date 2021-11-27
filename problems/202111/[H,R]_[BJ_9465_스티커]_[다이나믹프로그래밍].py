# BJ 9465 스티커 <다이나믹 프로그래밍>
# https://www.acmicpc.net/problem/9465
# 시간 : 60+
# 문제 리뷰 : H,R
# 회고 : 다이나믹 프로그래밍을 푸는 하나의 유형이다. 리스트 내에 그 위치의 최댓값을 저장하고 이를 모든 위치에 대해 구하는 방식이다.


T = int(input())
for _ in range(T):
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(2)]
    
    if n == 1:
        print(max(s[0][0], s[1][0]))

    else:
        s[0][1] += s[1][0]
        s[1][1] += s[0][0]  
        for i in range(2, n):
            s[0][i] += max(s[1][i-1], s[1][i-2])
            s[1][i] += max(s[0][i-1], s[0][i-2])
        
        print(max(s[0][n-1], s[1][n-1]))