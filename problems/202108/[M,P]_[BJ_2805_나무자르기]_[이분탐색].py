# BJ 2805 나무 자르기 <이분 탐색>
# https://www.acmicpc.net/problem/2805
# 시간 : 20
# 문제 리뷰 : M, P
# 회고 : 이분 탐색을 이전에 경험해봤기 때문에 비교적 쉽게 처리할 수 있었다.
#        아직 조건에 맞게 ans를 뽑는 것을 돌려보며 하였고 이분 탐색을 써야 한다는 것을 문제 유형을 보고 알았지만
#        해보면서 생각할 수 있도록 해야겠다.


N,M = map(int, input().split())
ls = list(map(int, input().split()))
ans,s,e = 0,0, max(ls)
while s <= e:
    m = (s+e)//2
    t = sum(map(lambda x:x-m if x>m else 0, ls))
    print(s,e, m, t)
    if t >= M: 
        s = m + 1
        ans = m
    elif t < M: 
        e = m - 1
print(ans)