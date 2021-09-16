# BJ 18870 좌표 압축 <정렬, 값/좌표압축>
# https://www.acmicpc.net/problem/18870
# 시간 : 10
# 문제 리뷰 : E,P
# 회고 : 


N,F,dic=input(),list(map(int,input().split())),{}
for i, n in enumerate(sorted(list(set(F)))):dic[n]=i
print(' '.join(map(str,([dic[n] for n in F]))))
