# BJ 2755 이번학기 평점은 몇점? <수학, 구현, 문자열, 사칙연산>
# https://www.acmicpc.net/problem/2755
# 시간 : 20
# 문제 리뷰 : M, R
# 회고 : 파이썬의 round가 특정 조건일 때 0.005이어도 올림 처리가 안되는 것과 0을 더해서 무조건 소수점 둘째까지 나타내야 하는 것이 까다로운 문제
#        Best Short Code에서 학점은 아스키 값의 변환을 통해 나타내었고 반올림은 나올 수 있는 경우의 수에서 반올림이 될 수 있는 경우를 생각한 창의적인 코드였다


a = {'A':4, 'B':3, 'C':2, 'D':1}
b = {'+':0.3, '0':0, '-':-0.3}
n = int(input())
g,t = 0,0
for _ in range(n):
    x,y = input().split()[1:]
    g += (a[y[0]]+b[y[1]])*int(x) if y!='F' else 0
    t += int(x)
print(f'{(int(g*100/t)+1)/100 if g*100/t-int(g*100/t)>=0.5 else int(g*100/t)/100:.2f}')


''' Best Short Code
f=lambda s:0 if s=='F'else((69-ord(s[0]))+[.3,0,-.3]['+0-'.index(s[1])]);l=0;s=0
for _ in range(int(input())):r=input().split();t=int(r[1]);l+=t;s+=t*f(r[2])
print('%.2f'%(s/l+0.0005))
'''