# BJ 2751 수 정렬하기 2 <정렬>
# https://www.acmicpc.net/problem/2751
# 시간 : 20
# 문제 리뷰 : E, R
# 회고 : 백준에서 open으로 받으면 줄 단위로 들어오는 입력을 모두 받는다.
#        또한 print(*list)로 출력하면 줄 단위로 출력해야하는 문제를 해결할 수 있다.


import sys
input = sys.stdin.readline
for i in sorted([int(input()) for _ in range(int(input()))]):print(i)


'''Best Code
print(*sorted(map(int,[*open(0)][1:])))
'''