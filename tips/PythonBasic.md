# Python Basic Tips

## 파이썬 응용
- 리스트에서 True, False의 유무를 검사할 때는 sum(list)가 아닌 any, all(list) 사용
- 리스트에서 특정 요소를 기준으로 작은 요소의 수나 큰 요소의 수를 구할 땐 정렬 후 list(enumerate(list, start=1))에서 index 부분 값

<br>

## 파이썬 문법
### 리스트
- `list.insert(index, value)`
- `list.extend(list)`
- `list.remove(value)`
- `list.reverse()`	or `reversed(list)`
- `list.count(value)`
- `list.index(value)`
- `' '.join(list)`
- `list[1:3] = [1, 2]` 	# 여러 요소를 리스트에 넣기
- `list.sort(key = lambda x : (x[0], -x[1]))`	# 다중 조건 정렬

### 문자열
- `string.find(찾을 요소, 시작 지점=0)`
- `string.startswith(시작하는문자, 시작 지점 =0)`
- `string.endswith(끝나는문자, 시작 지점 =0. 끝지점 = len(list))`
- `string.count(value)`
- `string.lower()`	
- `string.upper()`	
- `string[::-1]`		or `string.swapcase()`
- `reversed(string)`
- `string = string.replace("바꿀 요소", "바꾸는 요소")`
    - `string.replace('a','b',2)`: 'a'를 'b'로 바꾸는데 2번째까지만 바꿈
- `string.split(' ')` 	
- `string = string.lstrip("")`
- `string = string.rstrip("")`
- `string = string.strip("")`

### 진수 변환, 문자열 변환
- `format(42, 'b')`	# 이진수, bin(42) → '0b101010'	
- `format(42, 'o')`	# 8진수, oct(42) → '0o52'
- `format(42, 'x')`	# 16진수, hex(42) → '0x2a'
- `format(42, 'd')`	# 10진수, str(0b101010) → '42'
- `bin(0b101010)`

### 비트 연산
- `10|42`
- `10&42`

### 알파벳, 숫, 소문자, 대문자 여부
- `string.isalpha()`
- `string.isdigit()`
- `string.islower()`
- `string.isupper()`

### 아스키 변환
- `chr()`
- `ord()`

### 자리 수 채우기
- `"123".zfill(5)` : "00123" 반환
- `"123".rjust(5, "a")` : "aa123" 반환
- `ljust()`
- `center()`

### 딕셔너리
- `dict = {}`
- `dict['a'] = 1`
- `dict.keys()`
- `dict.values()`
- `dict.items()`

### 집합 자료형
- `set(list)`
- `set.add(value)`
- `set.update(list)`
- `set.remove(value)`
- &, |, -로 교집합, 합집합, 차집합 연산 가능

### any, all
- `any` : 리스트의 True가 하나라도 있으면 True
- `all` : 리스트가 모두 True여야 True

<br>

## 파이썬 예제
### 소수찾기
``` python
def is_prime(n):
    return all([(n%x) for x in range(2, int(n**0.5)+1)]) and n>1
```

### n까지의 수 중 소수 개수 찾기 (에라토스테네스의 체)
``` python
def solution(n):
    lst = set(range(2, n+1))
    
    for i in range(2, n+1):
        if i in lst:
            lst -= set(range(i**2, n+1, i))
    
    return len(lst)
```

### 최대공약수, 최소공배수 찾기 (유클리스 호제법)
``` python
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer
```

### 최대공약수 (a<b)
``` python
def gcd(a, b):
    return b if a == 0 else gcd(b%a,a)
```

### 최소공배수 (a<b)
``` python
def lcm(a, b):
    return a*b//gcd(a,b)
```

### 피보나치
``` python
def solution(n):
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b
```