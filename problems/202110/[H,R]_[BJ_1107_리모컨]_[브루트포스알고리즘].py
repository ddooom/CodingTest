# BJ 1107 리모컨 <브루트포스 알고리즘>
# https://www.acmicpc.net/problem/1107
# 시간 : 60+
# 문제 리뷰 : H,R
# 회고 : 반례가 너무 많아서 오래 걸린 문제
#        본인의 풀이는 이해하기 쉬우나 0부터 10**len(str(N))*2까지 다 해보는 알고리즘이기 때문에 매우 비효율적
#        효율적이지만 복잡한 식은 문제 풀이에 여러 방식으로 나와있다.


N = int(input())
M = int(input())
B = list(map(int, input().split())) if M!=0 else 0

if M == 0:
    print(min(len(str(N)), abs(N-100)))

else:
    answer = 5000000

    for i in range(10**len(str(N))*2):
        
        b = False
        for d in str(i):
            if int(d) in B:
                b = True
                break

        if b: continue
        answer = min(answer, abs(N-i)+len(str(i)))

    print(min(answer, abs(N-100)))