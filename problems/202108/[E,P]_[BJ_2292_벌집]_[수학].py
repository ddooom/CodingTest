# BJ 2292 벌집 <수학>
# https://www.acmicpc.net/problem/2292
# 시간 : 10
# 문제 리뷰 : E, P
# 회고 : Best Code처럼 수학적 접근으로 해결할 수 있다.


n=int(input())-1
for i in range(0, 20000):
    n-=i*6
    if n<=0: 
        print(i+1)
        break        

''' Best Code
print(int((int(input())/3-.1)**.5+1.5))
'''