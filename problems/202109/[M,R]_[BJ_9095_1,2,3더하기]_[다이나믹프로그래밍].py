# BJ 9095 1,2,3 더하기 <다이나믹 프로그래밍>
# https://www.acmicpc.net/problem/9095
# 시간 : 20
# 문제 리뷰 : M,R
# 회고 : 본인은 재귀함수를 사용하여 문제를 해결하였다.
#        하지만 Faster Answer은 n이 11보다 작은 수로만 나온다는 것을 이용하여 1부터 11까지의 답을 미리 구해놓았다.
#        해당 답은 이전 3개의 대한 답의 합이다. 예를 들어 n이 5일 때 답은 n이 4, 3, 2일 때 답의 합이다.
#        그 이유는 5는 결국 4의 경우들에 1을 더한 것이고, 3의 경우들에 2를 더한 것이고, 2의 경우들에 3을 더한 것이기 때문이다.


def solution(n):
    a,b,c=0,0,0
    if n>3: return solution(n-1)+solution(n-2)+solution(n-3)
    if n==1: return 1
    if n==2: return 2
    if n==3: return 4

N=int(input())
for _ in range(N):
    print(solution(int(input())))


''' Faster Answer
N = int(input())
arr=[1,2,4]
for i in range(4,11):
    arr.append(sum(arr[-3:]))
for _ in range(N):
    T = int(input())
    print(arr[T-1])
'''