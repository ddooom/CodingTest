# BJ 2456 나는 학급회장이다 <구현, 정렬>
# https://www.acmicpc.net/problem/2456
# 시간 : 40
# 문제 리뷰 : M, R
# 회고 : set를 이용해서 회장이 두 명 이상이면 다음 조건을 만족하지 않는 집합을 차집합하여 회장을 골라낸다.
#        Short Coding은 입력 받은 점수를 회장 별로 정렬한 뒤, 합과 3의 수, 2의 수를 기준으로 max를 구해 해당 값의 인덱스로 답을 찾았다.


n = int(input())
vt = {1:0, 2:0, 3:0}
vt3 = {1:0, 2:0, 3:0}
vt2 = {1:0, 2:0, 3:0}

for _ in range(n):
    inp = list(map(int, input().split()))
    for i in range(3):
        vt[i+1] += inp[i]
    vt3[inp.index(3)+1] += 1
    vt2[inp.index(2)+1] += 1

m = max(vt.values())
p = set([k for k, v in vt.items() if v == m])
if len(p) > 1: p -= set([k for k, v in vt3.items() if v != max(vt3.values())])
if len(p) > 1: p -= set([k for k, v in vt2.items() if v != max(vt2.values())])

print(f'{list(p)[0]} {m}' if len(p) == 1 else f'0 {m}')


''' Short Coding
s = [*map(sorted, zip(*[[*map(int, input().split())] for _ in range(int(input()))]))]
tt = max(s, key=lambda x: (sum(x), x.count(3), x.count(2)))
print(s.index(tt) + 1 if s.count(tt) == 1 else 0, sum(tt))
'''