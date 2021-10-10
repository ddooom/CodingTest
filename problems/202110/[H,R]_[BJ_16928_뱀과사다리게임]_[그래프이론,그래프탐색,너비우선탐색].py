# BJ 16928 뱀과 사다리 게임 <그래프 이론, 그래프 탐색, 너비 우선 탐색>
# https://www.acmicpc.net/problem/16928
# 시간 : 60+
# 문제 리뷰 : H,R
# 회고 : 아직도 무엇 때문에 Wrong Code가 틀렸는지 명확히 알지 못했다.
#       맞은 코드는 뱀과 사다리를 고려하여 이동할 경로를 movalbe로 정의한 뒤, bfs를 하는 것이었고
#       Wrong Code는 일단 1부터 6까지 이동하고 그 과정에서 뱀과 사다리가 있으면 처리하는 코드였다. 


P = {}
for _ in range(sum(map(int, input().split()))):
    a, b = (map(int, input().split()))
    P[a] = b

queue = [(1,0)]
check = [0] * 100
check[1] = 1
answer = 101

while queue:
    n, cnt = queue.pop(0)
    movable = [P[i] if i in P.keys() else i for i in range(n+1, n+7)]
    print(n, cnt, answer)
    
    for i in movable:
        if i == 100: answer = min(answer, cnt+1)
        
        elif (i<100) and not check[i]:
            check[i] = 1
            queue.append((i, cnt+1))

print(answer)


''' Wrong Code
P = {}
for _ in range(sum(map(int, input().split()))):
    a, b = (map(int, input().split()))
    P[a] = b

queue = [(1,0)]
check = [0] * 100
ans = 101
while queue:
    n = queue.pop(0)
    
    for i in range(1,7):
        if n+i == 100:
            ans = min(ans, check[n]+1)
            break
        
        if n+i in P.keys() and not check[P[n+i]]:
            check[n+i] = check[n] + 1
            check[P[n+i]] = check[n] + 1
            queue.append(P[n+i])
        
        elif not check[n+i]:
            check[n+i] = check[n] + 1
            queue.append(n+i)
    print(n, '\n', queue, '\n', [check[i] for i in queue], '\n')
print(ans)
'''