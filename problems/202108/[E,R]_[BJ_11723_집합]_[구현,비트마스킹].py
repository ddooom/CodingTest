# BJ 11723 집합 <구현, 비트마스킹>
# https://www.acmicpc.net/problem/11723
# 시간 : 15
# 문제 리뷰 : E, R
# 회고 : set를 상속받는 class로 add와 remove의 기능을 그대로 상속받으려고 했으나 all과 empty를 구현하지 못하였다.
#        set에서 remove(x) 연산은 set에 x가 없으면 에러가 떠 discard(x)를 사용해주어야 한다.


import sys
input = sys.stdin.readline

s = set()
for _ in range(int(input())):
    i = input().split()
    if i[0]=='add': s.add(int(i[1]))
    elif i[0]=='remove': s.discard(int(i[1]))
    elif i[0]=='check': print(1 if int(i[1]) in s else 0)
    elif i[0]=='toggle': 
        if int(i[1]) in s: s.remove(int(i[1]))
        else: s.add(int(i[1]))
    elif i[0]=='all': s = set(range(1,21))
    elif i[0]=='empty': s = set()
    