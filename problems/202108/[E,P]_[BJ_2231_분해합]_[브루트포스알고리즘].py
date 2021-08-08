# BJ 2231 분해합 <브루트포스 알고리즘>
# https://www.acmicpc.net/problem/2231
# 시간 : 10
# 문제 리뷰 : E, P
# 회고 : Pythonic Code를 보면 더 짧게 구현 가능하다. 반복문을 그냥 range(n)으로 하면 더욱 짧아진다.
#        하지만 값을 하나 찾았을 때 반복문을 break하지 않아 효율적이지 않을 수도 있으나 애초에 반복문이 짧아서 큰 상관 없을 듯하다. 


n = int(input())
a = 0
for i in range(max(n-9*len(str(n)),0),n+1):
    if i+sum(map(int,str(i))) == n: 
       a = i
       break
print(a) 


''' Pythonic Code
n = int(input())
print(([i for i in range(max(n-9*len(str(n)),0),n+1) if i+sum(map(int,str(i)))==n]+[0])[0])
'''