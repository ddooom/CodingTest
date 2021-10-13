# BJ 14500 테트로미노 <구현, 브루트포스 알고리즘>
# https://www.acmicpc.net/problem/14500
# 시간 : 40
# 문제 리뷰 : H,R
# 회고 : 본인은 단순하게 모든 경우의 수를 직접 구하여 최댓값을 구했다.
#        하지만 Faster Code의 경우에는 bfs를 구현하였다. 여기서 중요한 점은 제약 조건들을 이용하여 step이 4 이전에 끝낼 수 있는 조건문을 만들었다는 것이다.
#        함수 내에 해당 조건문이 없는 경우에는 시간 초과로 오답처리 된다. 


import sys
input = sys.stdin.readline

def search(r, c):
    lst = [0]
    
    if c+3 < M:
        lst.append(F[r][c]+F[r][c+1]+F[r][c+2]+F[r][c+3])
    
    if c+2 < M and r+1 < N:
        lst.append(F[r][c]+F[r][c+1]+F[r][c+2]+F[r+1][c+2])
        lst.append(F[r][c]+F[r][c+1]+F[r][c+2]+F[r+1][c+1])
        lst.append(F[r][c]+F[r][c+1]+F[r][c+2]+F[r+1][c])
        lst.append(F[r][c]+F[r+1][c]+F[r+1][c+1]+F[r+1][c+2])
        lst.append(F[r][c+1]+F[r+1][c]+F[r+1][c+1]+F[r+1][c+2])
        lst.append(F[r][c+2]+F[r+1][c]+F[r+1][c+1]+F[r+1][c+2])
        lst.append(F[r][c]+F[r][c+1]+F[r+1][c+1]+F[r+1][c+2])
        lst.append(F[r+1][c]+F[r+1][c+1]+F[r][c+1]+F[r][c+2])
    
    if c+1 < M and r+1 < N:
        lst.append(F[r][c]+F[r][c+1]+F[r+1][c]+F[r+1][c+1])
    
    if c+1 < M and r+2 < N:
        lst.append(F[r][c]+F[r][c+1]+F[r+1][c]+F[r+2][c])
        lst.append(F[r][c]+F[r+1][c+1]+F[r+1][c]+F[r+2][c])
        lst.append(F[r][c]+F[r+2][c+1]+F[r+1][c]+F[r+2][c])
        lst.append(F[r][c]+F[r][c+1]+F[r+1][c+1]+F[r+2][c+1])
        lst.append(F[r+1][c]+F[r][c+1]+F[r+1][c+1]+F[r+2][c+1])
        lst.append(F[r+2][c]+F[r][c+1]+F[r+1][c+1]+F[r+2][c+1])
        lst.append(F[r][c]+F[r+1][c]+F[r+1][c+1]+F[r+2][c+1])
        lst.append(F[r][c+1]+F[r+1][c+1]+F[r+1][c]+F[r+2][c])
        
    if r+3 < N:
        lst.append(F[r][c]+F[r+1][c]+F[r+2][c]+F[r+3][c])
    
    return max(lst) 

N,M = map(int, input().split())
F = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for r in range(N):
    for c in range(M):
        answer = max(answer, search(r,c))

print(answer)


''' Faster Code
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
F = [list(map(int, input().split())) for _ in range(N)]

answer = 0
def bfs(trace, add, step):
    global answer
    
    if step == 4:
        answer = max(answer, add)
        return (0)
    elif step == 1 and add < answer - 3000: return (0)
    elif step == 2 and add < answer - 2000: return (0)
    elif step == 3 and add < answer - 1000: return (0)
        
    way = []
    for loc in trace:
        r, c = loc
        if r > 0: way.append((r-1,c))
        if r < N-1: way.append((r+1,c))
        if c > 0: way.append((r,c-1))
        if c < M-1: way.append((r,c-1))
            
    for loc in way:
        if loc in trace:
            continue
        r, c = loc
        bfs(trace+[loc], add+F[r][c], step+1)

for r in range(N):
    for c in range(M):
        bfs([(r,c)], F[r][c], 1)
        
print(answer)
'''