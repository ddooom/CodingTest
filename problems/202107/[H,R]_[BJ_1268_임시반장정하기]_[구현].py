# BJ 1268 임시 반장 정하기 <구현>
# https://www.acmicpc.net/problem/1268
# 시간 : 20
# 문제 리뷰 : H, R
# 회고 : 나의 풀이의 시간 복잡도는 5*n*n이고 Best Answer의 시간복잡도는 5*n으로 실행시간이 약 50배 차이났다.
#        Best Answer는 set을 이용하여 학생의 반을 index로 하고 set 안에 학생을 넣었다.
#        따라서, 특정 학생의 반을 index로 하여 set에 접근하면 해당 set 안에는 같은 반이었던 학생들이 있는 것이다.
#        이 학생들을 5개에 반에 대해 교집합하면 특정 학생과 같은 반이었던 학생들이 중복 없이 구해지게 된다.
#        그에 반해, 나의 풀이는 특정 학생이 5개 반 별로 모든 학생들과 같은 반인지 확인하기 때문에 5*n*n이고 느리다.
#        Best Answer 같은 사고가 필요하다.


import sys
input = sys.stdin.readline
n = int(input())
data = list(zip(*[input().rstrip().split() for _ in range(n)]))
cnts = []
for s in range(n):
    students = [s for s in range(n)]
    for c in range(5):
        for o in range(n):
            if data[c][s] == data[c][o] and o in students:
                students.remove(o)
    cnts.append(len(students))

print(cnts.index(min(cnts))+1)


''' Best Answer
import sys
input = sys.stdin.readline
n = int(input())
students = []
dist = [[set() for _ in range(10)] for _ in range(5)]
cnts = []

for s in range(n):
    student = list(map(int, input().rstrip().split()))
    students.append(student)
    for c in range(5):
        dist[c][student[c]].add(s) 

for s in range(n):
    cnt = set()
    for c in range(5):
        cnt |= dist[c][students[s][c]]
    cnts.append(len(cnt))

print(cnts.index(max(cnts))+1)

'''