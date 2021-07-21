# BJ 1834 나머지와 몫이 같은 수 <수학>
# https://www.acmicpc.net/problem/1834
# 시간 : 10
# 문제 리뷰 : E, R
# 회고 : 주석의 1번 방법을 통해 조건에 맞는 수들의 규칙성을 찾은 뒤, 2번 코드를 도출하였다.
#        2번 또한 같은 수의 간격으로 이루어져 있어 더한 값이 n으로 표현될 수 있었다.


n = int(input())
print((n**3-n)//2)


'''
1. print([i for i in range(1, n*n) if i//n == i%n])

2. print([i for i in range(n+1, n*n, n+1)])
'''

