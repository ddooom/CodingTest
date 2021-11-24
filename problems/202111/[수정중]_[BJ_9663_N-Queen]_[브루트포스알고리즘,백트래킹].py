# BJ 9663 N-Queen <브루트포스 알고리즘, 백트래킹>
# https://www.acmicpc.net/problem/9663
# 시간 : [경과 시간]
# 문제 리뷰 : [문제 리뷰]
# 회고 : [회고]

def possible(row_idx, col_idx, other):
    if row_idx == other[0]:
        return False
    if col_idx == other[1]:
        return False
    if abs((row_idx-other[0])/(col_idx-other[1])) == 1:
        return False
    return True


def search(row_idx, col_idx, visit):
    global answer
    if row_idx == (N-1):
        answer += 1
        return 0
    
    for i in list(range(0, col_idx-1)) + list(range(col_idx+2, N)):
        recur = True
        for j in range(0, len(visit)-1):
            if not possible(row_idx+1, i, visit[j]):
                recur = False
                break
        if recur:
            search(row_idx+1, i, visit + [[row_idx+1, i]])


N = int(input())
answer = 0
for col_idx in range(N):
    visit = []
    search(0, col_idx, [[0, col_idx]])
    
print(answer)