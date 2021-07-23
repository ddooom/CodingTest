# BJ 1977 완전제곱수 <수학, 구현>
# https://www.acmicpc.net/problem/1977
# 시간 : 10
# 문제 리뷰 : E, P
# 회고 : 입력 값에 따라 범위가 달라지게 설정했지만, 수의 범위가 작아
#        1부터 100까지 순회하며 조건에 맞는 제곱수를 찾아도 실행 속도가 빠를 것 같다.


a, b = int(input()), int(input())
data = [i**2 for i in range(int(-1*((-1*a**(1/2))//1)), int(b**(1/2))+1)]
print(f'{sum(data)}\n{min(data)}' if len(data) > 0 else -1)