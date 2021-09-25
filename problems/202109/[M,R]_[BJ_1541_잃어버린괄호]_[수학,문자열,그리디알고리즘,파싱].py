# BJ 1541 잃어버린 괄호 <수학, 문자열, 그리디 알고리즘, 파싱>
# https://www.acmicpc.net/problem/1541
# 시간 : 30
# 문제 리뷰 : M, R
# 회고 : 그리디 알고리즘이라 하나씩 연산해야하나 했지만, 인덱스 문제로 어려움을 겪고 있었다.
#        하지만, 그냥 덧셈부터 한 뒤 뺄셈을 하면 되는 것이었다.


t = []
for i in input().split('-'):
    if '+' in i: t.append(sum(map(int, i.split('+'))))
    else: t.append(int(i))
print(t[0]-sum(t[1:]))


''' Pythonic Code
l=[sum(map(int,s.split('+'))) for s in input().split('-')]
print(l[0]-sum(l[1:]))
'''