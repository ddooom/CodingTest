# BJ 2775 부녀회장이 될테야 <수학>
# https://www.acmicpc.net/problem/2775
# 시간 : 15
# 문제 리뷰 : E, R
# 회고 : '수학' 문제는 문제의 조건대로 구현 후, 수학적 규칙성을 찾아야 한다.
#        이번 경우 조합이라는 규칙성을 찾지 못했다. 조합의 규칙성을 머리 속에 넣어둬야할 것 같다.


# 0 : 1 2 3  4  5  6   7
# 1 : 1 3 6  10 15 21  28
# 2 : 1 4 10 20 35 56  84
# 3 : 1 5 15 35 70 126 210
# ...

# (k, n) = (k, n-1) + (k-1, n)
#        = (k, n-2) + 2*(k-1, n-1) + (k-2, n) 
#        ...

iter = int(input())
for _ in range(iter):
    k, n = int(input()), int(input())
    l = [[i+1 for i in range(n)]]
    for f in range(k):
        l.append([sum(l[-1][:i+1]) for i in range(n)])
    print(l[-1][-1])


''' Best Code
import math
i=input
for n in[int]*int(i()):k=n(i());print(math.comb(k+n(i()),k+1))
'''