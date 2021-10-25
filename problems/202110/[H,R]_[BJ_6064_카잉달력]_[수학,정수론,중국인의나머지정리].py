# BJ 6064 카잉 달력 <수학, 정수론, 중국인의 나머지 정리>
# https://www.acmicpc.net/problem/6064 
# 시간 : 60+
# 문제 리뷰 : H,R
# 회고 : 시간 복잡도를 신경 쓰지 않고 알고리즘 자체를 구현한 다음, 해당 알고리즘을 출력하여 패턴을 파악하였다.
#        이후에 수학적 패턴을 발견하여 간단한 수식이나 반복문으로 구현하려 하였다.


for _ in range(int(input())):
    M,N,x,y = map(int, input().split())

    if M < N: M,N,x,y = N,M,y,x

    through = True
    for i in range(M):
        if y == (x+(M-N)*i-1)%N+1:
            print(x+M*i)
            through = False
            break

    if through:print(-1)