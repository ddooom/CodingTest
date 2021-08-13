# BJ 10828 스택 <자료 구조, 스택>
# https://www.acmicpc.net/problem/10828
# 시간 : 15
# 문제 리뷰 : E, P
# 회고 : 간단한 스택문제를 클래스를 이용하여 풀어보았다.

class stack():
    def __init__(self):
        self.s = []
    def push(self, n):
        self.s.append(n)
    def pop(self):
        print(self.s.pop(-1) if len(self.s)!=0 else -1)
    def size(self):
        print(len(self.s))
    def empty(self):
        print(int(len(self.s)==0))
    def top(self):
        print(self.s[-1] if len(self.s)!=0 else -1)
        
import sys
input = sys.stdin.readline
s = stack()
for _ in range(int(input())):
    i = input().rstrip()
    if i[:2]=='pu': getattr(s, "push")(int(i.split()[1]))
    else: getattr(s, i)()