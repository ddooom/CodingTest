# BJ 2579 계단 오르기 <다이나믹 프로그래밍>
# https://www.acmicpc.net/problem/2579
# 시간 : 60
# 문제 리뷰 : H,R
# 회고 : DP의 시작은 마지막 값이 앞에 어떤 DP 값과 입력받은 값이 이용되는지를 파악해야 한다.
#        이 문제 같은 경우는 3번 연속 한개씩 오를 수 없다는 것을 이용하여 
#        i번째 최댓값은 i-2번째의 최댓값에 i번째 계단 값을 더한 것이거나 i-3번째 최댓값에 i-1, i번째 계단 값을 더한 것이다라는 것을 파악해야 한다.

#        Best Answer 또한 같은 알고리즘이나 입력 받은 리스트의 길이 조건 없이 값을 찾을 수 있도록 구현한 것이다. 이해하기 어렵다..


l = [int(input()) for _ in range(int(input()))]
if len(l) < 3:
    print(sum(l))
else:
    dp = [l[0], l[0]+l[1], max(l[0]+l[2],l[1]+l[2])]
    for i in range(3, len(l)):
        dp.append(max(l[i]+l[i-1]+dp[i-3], l[i]+dp[i-2]))
    print(dp[-1])


''' Best Answer
from sys import stdin

a,b,c = 0,0,0

n = int(stdin.readline())
for _ in range(n):
    pb = int(stdin.readline())
    d_0,d_1,d_2 = max(b,c),a+pb,b+pb
    a,b,c = d_0,d_1,d_2

print(max(d_2,d_1))
'''