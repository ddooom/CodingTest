# BJ 1436 영화감독 숌 <브루트포스 알고리즘>
# https://www.acmicpc.net/problem/1436
# 시간 : 10
# 문제 리뷰 : E, R
# 회고 : 조건에 맞을 때까지 1씩 더하는 비효율적이지만 짧으 코드를 작성하였다.
#        시간 복잡도를 따지고 긴 코드를 구성하도록 다시 풀 필요가 있다.


n = int(input())
s = 666
m = 0
while 1:
    if '666' in str(s): m+=1
    if m == n: 
        print(s)
        break
    s+=1