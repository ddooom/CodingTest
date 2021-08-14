# BJ 1929 소수 구하기 <수학, 정수론, 소수 판정, 에라토스테네스의 체>
# https://www.acmicpc.net/problem/1929
# 시간 : 20
# 문제 리뷰 : M, R
# 회고 : 기존 에라토스테네스의 체 알고리즘을 알고 있었기에 어렵지 않게 풀 수 있었다.
#        범위 조정을 통해 더 빠른 코드를 할 수 있을 것 같다.
#        set()를 그대로 list()로 바꾸어도 순서가 유지되지 않는다.
#        Faster Code의 알고리즘은 아직 이해하지 못하겠다...


M,N=map(int,input().split())
s = set(range(2,N+1))
for i in range(2, N+1):
    if i in s:
        s -= set(range(i**2, N+1, i))

for i in sorted(list(s)): 
    if i >= M: print(i)
    if i > N: break


''' Faster Code
m, n = map(int, input().split())
li = [False] + [True] * ((n - 1) // 2)
for x in range(1, int(n**.5/2+1)):
    if li[x]:
        li[2*x*(x+1)::x*2+1] = [False] * ((((n + 1) // 2) - x * x * 2) // (x * 2 + 1))
if m <= 2:
    print(2)
print('\n'.join([f'{x}' for x, val in zip(range(m+(m&1==0), n+1, 2), li[m//2:]) if val]))
'''