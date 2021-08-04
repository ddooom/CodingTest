# BJ 1978 소수 찾기 <수학, 정수론, 소수판정, 에라토스테네스의 채>
# https://www.acmicpc.net/problem/1978
# 시간 : 10
# 문제 리뷰 : E, R
# 회고 : 에라토스테네스의 채를 알고 있다면 쉽게 풀이할 수 있는 문제
#        에라토스테네스의 채를 이용해 처음 한 번만 범위 내에서 소수를 찾고 입력 값이 소수인지를 찾는 방법을 사용
#        하지만 Short Coding이나 다른 효율적인 방법은 하나 하나 2부터 n까지 나머지가 0인지 확인하며 소수인지 찾는 방법 사용
#        Short Coding에서 이중 조건은 * 사용하였고, 모두 나눠지지 않는 조건은 all을 사용함
 

def prime(n):
    p = set(range(2, n+1))
    for i in range(2, n+1):
        if i in p:
            p -= set(range(i**2, n+1, i))
    return p

n,l=input(),list(map(int,input().split()))
p=prime(max(l))
print(sum(map(lambda x:x in p, l)))


''' Short Coding
input();print(sum(all(n%j for j in range(2,n))*n>1for n in map(int,input().split())))
'''