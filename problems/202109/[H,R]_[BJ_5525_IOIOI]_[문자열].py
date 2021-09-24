# BJ 5525 IOIOI <문자열>
# https://www.acmicpc.net/problem/5525
# 시간 : 30
# 문제 리뷰 : H,R
# 회고 : 처음에 시도한 것은 문자열 S의 요소를 하나씩 탐색하며 IOI를 찾는 것 이었다. 이 경우 시간복잡도는 N*M으로 N,M이 커질 때 시간초과로 50점이다.
#        하지만, 문자열 S만 탐색하는 즉, 시간복잡도가 M인 100점짜리 코드는 한번의 반복문으로 IOI인 것을 찾고 N만큼의 길이가 되면 p에서 빼는 식으로 진행한다.
#        마지막으로 Faster Code는 붙어있는 IOI의 길이를 통해 한번에 답을 구할 수 있는 것을 이용하여 IOI를 X로 변환하여 X의 길이로 답을 구하였다.


'''
My Code : 50점
'''

P,M,S='I'+'OI'*int(input()),input(),input()
L=len(P)
c=0
for i in range(len(S)-L):
    if S[i:i+L]==P:c+=1
print(c)


''' 100점 Code
N,M,S=int(input()),int(input()),input()
i=c=p=0
while i<M-2:
    if (S[i]=='I') and (S[i+1]=='O') and (S[i+2]=='I'):
        p+=1
        if p==N:
            c+=1
            p-=1
        i+=1
    else:
        p=0
    i+=1
print(c)
'''


''' Faster Code
N,M,S=int(input()),int(input()),input()
i=c=p=0
while i<M-2:
    if (S[i]=='I') and (S[i+1]=='O') and (S[i+2]=='I'):
        p+=1
        if p==N:
            c+=1
            p-=1
        i+=1
    else:
        p=0
    i+=1
print(c)
'''