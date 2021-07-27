# BJ 2456 나는 학급회장이다 <구현, 정렬>
# https://www.acmicpc.net/problem/2456
# 시간 : [경과 시간]
# 문제 리뷰 : [문제 리뷰]
# 회고 : [회고]

n = int(input())
d = [[1,2,3], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
for _ in range(n):
    inp = list(map(int, input().split()))
    for i in range(3):
        d[0][i] += inp[i]
    
    d[1][inp.index(3)] += 1
    d[2][inp.index(2)] += 1

m1 = max(d[1])
if d[1].count(m1) == 1:
    print(f'{d[0][d[1].index(m1)]} {m1}')
else:
    c = list(zip(*d))
    for i in range(len(d[0])):
        if d[1][i] != m1: c.pop(i)
    d = list(zip(*c))
    
    m2 = max(d[2])
    if d[1].count(m2) == 1:
        print(f'{d[0][d[2].index(m2)]} {m1}')
    else:
        c = list(zip(*d))
        for i in range(len(d[0])):
            if d[2][i] != m2: c.pop(i)
        d = list(zip(*c))
        
        m3 = max(d[3])
        if d[2].count(m3) == 1:
            print(f'{d[0][d[3].index(m3)]} {m1}')
        else:
            print(f'0 {m1}')

