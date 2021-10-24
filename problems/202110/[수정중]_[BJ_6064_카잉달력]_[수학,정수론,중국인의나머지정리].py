# BJ 6064 카잉 달력 <수학, 정수론, 중국인의 나머지 정리>
# https://www.acmicpc.net/problem/6064 
# 시간 : [경과 시간]
# 문제 리뷰 : [문제 리뷰]
# 회고 : [회고]


for _ in range(int(input())):
    M,N,x,y = map(int, input().split())
    
    a,b,n = 1,1,1
    while 1:
        if a==M and b==N:
            print(-1)
            break
        
        if a==x and b==y:
            print(n)
            break
        
        a = a%M+1
        b = b%N+1
        n += 1