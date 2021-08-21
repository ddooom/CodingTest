# BJ 1463 1로 만들기 <다이나믹 프로그래밍>
# https://www.acmicpc.net/problem/1463
# 시간 : 15
# 문제 리뷰 : M, R
# 회고 : 나는 연산 수의 따라 연산 결과들을 리스트에 추가하여 리스트에 1이 있으면 해당 단계의 연산 수를 출력하는 형식으로 풀이하였다.
#        하지만 Faster Code를 보면 dictionary에 수에 따른 연산 수를 저장하여 겹치는 수를 실행시간 없이 도출하였고
#        1을 빼는 연산은 나누어 떨어지지 않을 경우 3나 2을 나눈 나머지를 더해주는 형태로 작성하였다.
#        이를 재귀로 하여 2나 3으로 나눠진 값으로 dictionary를 탐색하거나 연산을 진행하고 결과적으로 수행시간이 적은 경우를 출력하였다.


ls = [int(input())]
ans = 0
while 1 not in ls:
    ans += 1
    tmp = []
    for i in ls:
        if i%3==0: tmp.append(i//3)
        if i%2==0: tmp.append(i//2)
        tmp.append(i-1)
        ls = tmp
print(ans)
    

''' Faster Code
def dp(n):
    if n in memo:
        return memo[n]
    m = 1 + min(dp(n // 2) + n % 2, dp(n // 3) + n % 3)
    memo[n] = m
    return m

memo = {1: 0, 2: 1}
n = int(input())
print(dp(n)).
'''