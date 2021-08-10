# BJ 10989 수 정렬하기 3 <정렬>
# https://www.acmicpc.net/problem/10989
# 시간 : 20
# 문제 리뷰 : M, R
# 회고 : 해당 문제는 메모리 제한이 있기 때문에 최대 10000000개의 수를 리스트에 담아 정렬하면 메모리 초과가 떴다.
#        따라서 입력받는 모든 수는 10000 이하라는 점을 이용해서 dictionary로 입력받는 수와 그 수의 개수를 나타내었고 이를 출력하였다.
#        출력 방식에서 sys.stdin.readline과 같이 sys.stdout.write('\n')를 사용하면 매우 빠르게 출력할 수 있었다.
#        또한, 내 코드와 같이 반복문으로 출력하는 방식보단 Faster Code처럼 100000개씩 묶어서 출력하는 것이 빨랐다.
#        Faster Code에선 리스트를 사용하였고 내 코드에서는 입력받는 수에 따른 dictionary를 사용하였는데, 대부분 모든 수가 입력된다면 리스트 형식이 몇몇 수만 입력된다는 dictionary 형식이 더 빠를 것이다.


import sys
from collections import defaultdict
input = sys.stdin.readline
d = defaultdict(int)
for _ in range(int(input())): d[int(input())] += 1
for n in sorted(d): 
    for _ in range(d[n]): print(n) 


''' Faster Code 
import sys
count=[0]*10000
for i in range(int(input())):
    count[int(sys.stdin.readline())-1]+=1
for i in range(10000):
    if count[i]!=0:
        while count[i]>100000:
            sys.stdout.write("%d\n" % (i+1)*100000)
            count[i]-=100000
        sys.stdout.write("%d\n" % (i+1)*count[i])
'''