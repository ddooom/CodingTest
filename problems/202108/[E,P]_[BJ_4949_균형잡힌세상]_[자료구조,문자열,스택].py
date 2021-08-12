# BJ 4949 균형잡힌 세상 <자료 구조, 문자열, 스택>
# https://www.acmicpc.net/problem/4949
# 시간 : 20
# 문제 리뷰 : E, P
# 회고 : 전형적인 스택을 사용하는 문제


while 1:
    s, c = [], input()
    if c == '.': break
    for i in c:
        if i in '[]()': s.append(i)
        if len(s)>1 and i==']' and s[-2]=='[': del s[-2:]
        if len(s)>1 and i==')' and s[-2]=='(': del s[-2:]
    print('yes' if len(s)==0 else 'no')
    
