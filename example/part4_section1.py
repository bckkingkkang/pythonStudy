a = 10
a += 2
print(a)

a = 10
a *= 2
print(a)

a = 10
b = 3
a += 2 * b  # a = a + (2 * b)
print(a)

# bit 는 0 또는 1로 표현할 수 있는 데이터의 단위이며, 컴퓨터에서 1byte는 8bit이다.

'''
int() : 정수형으로 변환, 소수점 이하 값은 내림
float() : 실수형으로 반환
str() : 문자열로 반환
'''

# 내장 함수 type()을 이용하여 자료형 확인
int(3.14)
float(3)
print(type(5))
print(type(3.14))
print(type('Good'))

kor = 86
eng = 87
math = 97
average = (kor + eng + math)/3
print(average)

# 실수 표현 : 부동 소수점 방식으로 표기
# 영문자 E 또는 e를 가운데 두고 왼쪽에 가수, 오른쪽에 지수를 쓴다.
print(3.14e2)   # 10의 2승
print(3.14e-2)  # 10의 -2승

a = 3.5214
n = 5
# 정수와 실수에서 자주 사용하는 내장 함수
print(abs(a))          # a의 절댓값 반환
print(divmod(a, b))    # a를 b로 나누었을 때의 몫과 나머지를 반환
print(pow(a, b))       # a를 b번 곱한 값을 반환한다. (a**b와 동일)
print(round(a, n))     # n이 양수이면 a를 반올림하여 소수점 n자리까지 나타내고 n이 음수이면 a를 n자리에서 반올림하여 반환

# 복소수는 실수와 허수로 이루어진 자료형으로 a + bj 형태로 표현한다.
# 내장함수 complex() 를 이용하면 복소수 형태로 나타낼 수 있다.
print(2 + 3j)
print(complex(2,3))
print((3+2j) + complex(2,5))

# bool 형
print(bool(0))  # false
print(bool(1))  # true
print(bool("Hello"))    # 문자열이 있으므로 true 반환