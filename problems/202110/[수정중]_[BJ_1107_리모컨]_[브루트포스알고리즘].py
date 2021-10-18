# BJ 1107 리모컨 <브루트포스 알고리즘>
# https://www.acmicpc.net/problem/1107
# 시간 : [경과 시간]
# 문제 리뷰 : [문제 리뷰]
# 회고 : [회고]


N = int(input())
M, B = input(), list(map(int, input().split()))

C = set([round(N, -i) for i in range(len(str(N))+1)])
A = [abs(N-100)]
for c in C:
    L = len(str(c))
    a = 0
    p = 0
    
    for l in range(L):
        t = int(str(c)[l])
        
        for n in range(10):
            if (t-n) not in B and (t-n)>0:
                a += (t-n) * 10**(L-l-1)
                p += 1
                break
            if (t+n) not in B and (t+n)<10:
                a += (t+n) * 10**(L-l-1)
                p += 1
                break
                
    A.append(abs(N-a)+p)

print(min(A))


'''
N = int(input())
M = int(input())
B = list(map(int, input().split())) if M!=0 else 0

if M == 0:
    print(abs(N-100))

else:

    answer = 10**len(str(N))
    for i in range(10**len(str(N))*2):
        
        b = False
        for d in str(i):
            if int(d) in B:
                b = True
                break

        if b: continue

        answer = min(answer, abs(N-i)+len(str(i)))

    print(min(answer, abs(N-100))
'''