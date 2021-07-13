# BJ 1157 단어 공부 <구현, 문자열>
# https://www.acmicpc.net/problem/1157
# 시간 : 10
# 문제 리뷰 : E, R
# 회고 : 문자열을 문자열 자체로 풀이하는 것보다 아스키코드로 처리하는 것이 더 빠른 처리다!!


word = input().upper()
dic = set(word)
max_cnt = 0
answer = ''
for w in dic:
    cnt = word.count(w)
    if cnt > max_cnt:
        max_cnt = cnt
        answer = w
    elif cnt == max_cnt:
        answer = '?'

print(answer)


''' Best 풀이
s,a=input().lower(),[]
for i in range(97,123):
a.append(s.count(chr(i)))
print('?'if a.count(max(a))>1 else chr(a.index(max(a))+97).upper())
'''