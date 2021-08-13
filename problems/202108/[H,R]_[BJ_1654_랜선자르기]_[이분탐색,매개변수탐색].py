# BJ 1654 랜선 자르기 <이분 탐색, 매개 변수 탐색>
# https://www.acmicpc.net/problem/1654
# 시간 : 50
# 문제 리뷰 : H, R
# 회고 : 처음에는 1부터 (s+e)//2까지 특정 수 단위로 탐색한 뒤, 그 단위 범위 내에서 1씩 줄여가며 찾았다.
#        하지만 해당 방법은 시간 초과로 인해서 오답이 되었고 이분 탐색을 사용하였다.
#        첫 이분 탐색 구현이라 범위 나누는 것이 서툴렀고 맞은 사람의 풀이르 보며 코드를 Modified Code와 같이 보완하였다.


import sys
input=sys.stdin.readline
n,k=map(int, input().split())
l=[int(input()) for _ in range(n)]
s,e=0,sum(l)//k
if ((s+e)//2)==0: print(1)
else:
    while 1:
        if sum(map(lambda x:x//((s+e)//2),l))>=k:s=(s+e)//2
        else: e=(s+e)//2
        if (s+1)==e: break
    print(e if sum(map(lambda x:x//e,l))>=k else s)


''' Modified Code
import sys
input=sys.stdin.readline
n,k=map(int, input().split())
l=[int(input()) for _ in range(n)]
s,e=1,sum(l)//k
while s<=e:
    m=(s+e)//2
    if sum(map(lambda x:x//((s+e)//2),l))>=k:s=m+1;ans=m
    else: e=m-1
print(ans)
'''