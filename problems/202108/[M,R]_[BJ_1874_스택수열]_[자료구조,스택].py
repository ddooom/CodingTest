# BJ 1874 스택 수열 <자료 구조, 스택>
# https://www.acmicpc.net/problem/1874
# 시간 : 30
# 문제 리뷰 : M, R
# 회고 : 코드 자체는 비효율적이었지만, 제한 시간이 빡세지 않아 맞을 수 있었다.
#        하지만, Faster Code를 보면 1~n까지의 수를 리스트로 처리하지 않고 cur=1 변수에 1씩 더해가며 처리하였다.
#        이는 1~n 까지의 리스트를 만드는 시간과 매번 이 리스트에 접근하여 스택에 push하는 과정을 없애준다.


import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
ls = [i+1 for i in range(n)]
t = [int(input()) for _ in range(n)]
s = []
ans = []

for i in t:
    if len(s)==0:
        s.append(ls.pop(0))
        ans.append('+')

    while 1:
        if s[-1] == i:
            s.pop(-1)
            ans.append('-')
            break

        elif len(ls)==0 and len(s)!=0:
            ans = ['NO']
            break

        s.append(ls.pop(0))
        ans.append('+')

    if ans == ['NO']: break

for a in ans: print(f'{a}\n')


''' Faster Code
import sys
input = sys.stdin.read

n, *nums = map(int, input().split())
cur = 1
st = []
answer = []
for num in nums:
    while cur <= num:
        st.append(cur)
        answer.append('+')
        cur += 1
    if st[-1] != num:
        answer = ['NO']
        break
    st.pop()
    answer.append('-')
print('\n'.join(answer))
'''