# BJ 1629 곱셈 <수학, 분할 정복을 이용한 거듭제곱>
# [문제 사이트 주소]
# 시간 : [경과 시간]
# 문제 리뷰 : [문제 리뷰]
# 회고 : [회고]


A,B,C = map(int, input().split())
compress = 1
i = 1
while i <= B:
    print(A,B,C, i, compress)
    if A ** i > C:
        compress *= A ** (11%i)
        A = A ** i % C
        B = B // i
        i = 1
    else:
        i += 1

print(compress*(A**B)%C)