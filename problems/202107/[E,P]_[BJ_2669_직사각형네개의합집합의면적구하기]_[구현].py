# BJ 2669 직사각형 네개의 합집합의 면적 구하기 <구현>
# https://www.acmicpc.net/problem/2669
# 시간 : 10
# 문제 리뷰 : E, P
# 회고 : set의 add를 활용한 유니크한 값 도출하였다.
#        이후 더 pythonic하게 개선할 수 있을 것 같아 코드를 짧게 개선하였다.


t = set()
for _ in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            t.add((i, j))

print(len(t))


''' My Pythonic Code
t = [list(map(int, input().split())) for _ in range(4)]
print(len({(i, j) for p in t for i in range(p[0],p[2]) for j in range(p[1],p[3])}))
'''

