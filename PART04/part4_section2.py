# 문자열은 한 글자 이상의 문자나 기호로 구성되며, 순서가 있는 문자들의 배열로 이루어진 시퀀스 자료형이다.
s = "Hello World!"
print(s)

s1 = "Let's go"
print(s1)

s2 = 'He said, "Be honest!"'
print(s2)

s3 = "No Pain,\nNo Gain"
print(s3)

s4 = '''
After a storm,
comes a calm.
'''
print(s4)

s5 = """
After a storm,
comes a calm.
"""
print(s5)

s6 = 'hello, ' + 'world'
print(s6)

# 동일한 문자열 반복
print(s1 * 4)

# in 키워드 : 자료에 어떤 값이 있는지 없는지 확인할 때 사용
print('e' in 'Lemon Tree')
print("Tree" in "Lemon Tree")

# 인덱싱과 슬라이싱
s = "Think different"
print(s[0])
print(s[5])
print(s[-4])

# 슬라이싱 : 문자열의 특정 구간의 값을 추출한다.
# 문자열[시작 : 끝]
s = "Have a Good Day!"
print(s[7] + s[8] + s[9] + s[10])
print(s[7:11])  # 문자열 인덱스 7부터 11 미만인 문자
print(s[:4])    # 문자열 처음부터 4미만의 문자 = s[0:4]
print(s[7:])    # 문자열 인덱스 7인 문자부터 끝까지
print(s[:-2])   # 문자열 처음부터 끝에서 두번재 미만까지
print([s[:]])   # 문자열의 처음부터 끝까지

# 문자열 슬라이싱에서 마지막에 스텝(폭)을 지정해 줄 수 있다.
# 스텝은 생략 가능하며 디폴트 값은 1이다. 설정한 숫자만큼 건너뛰며 문자를 추출한다.
print(s[::2])
print(s[::-1])  # 문자열 거꾸로 추출
print(s[3::3])

'''
문자열은 수정이 불가능하여 한 번 초기화되면 바꿀 수 없다.
문자열을 변경하기 위해서 슬라이싱 기능을 이용하여 원하는 문자로 연결하여 나타낼 수 있다.
'''
s = "Good Luck!"
# s[0] = 'g'   문자열 변경 불가능
s = 'g' + s[1:]
print(s)

# 문자열 포맷팅 : 문자열 안에 어떤 값을 삽입하는 방법
print("생일은 %d월입니다." %11)

birth = 10
print("생일은 %d월입니다." %birth)

s = "생일"
print("%s은 %d월 %d일입니다." %(s, birth, 14))    # 여러 개의 값 넣기

# format 함수를 이용하여 값을 삽입할 수 있다.
print("{} 주세요" .format("핫초코"))
print("커피 {}잔, 녹차 {}잔 주문" .format(2, 3))
print("오렌지 {a}개, 바나나 {b}개" .format(a=3, b=5))

# f문자열 포맷팅
fruit = "망고"
cnt = 5
print(f'{fruit} {cnt}개 주세요')

"""
len() : 문자열의 길이 반환, 문자열의 길이는 문자열의 개수를 의미한다.

find() : 찾고자 하는 문자를 검색하여 해당 문자의 위치를 반환한다. 해당 문자가 없을 경우 -1을 반환한다.
index() : 찾고자 하는 문자를 검색하여 해당 문자의 위치를 반환한다. 해당 문자가 없을 때는 예외가 발생한다.
count() : 특정 문자의 개수를 반환한다. 
"""

s = "Good Moring"
print(len(s))
print(s.find('o'))
print(s.index('i'))
print(s.find('j'))
# print(s.index('j'))   오류 발생
print(s.count('o'))

# 대소문자 변경
"""
    lower() : 영문자를 모두 소문자로 변경
    upper() : 영문자를 모두 대문자로 변경
    capitalize() : 문자열의 첫 글자만 대문자로 변경
"""
str = "Good Everning"
print(s.lower())
print(s.upper())
print(s.capitalize())

'''
공백 제거
    strip() : 문자열의 양쪽 공백 문자를 제거한다.
    lstrip() : 문자열의 왼쪽 공백 문자를 제거한다.
    rstrip() : 문자열의 오른쪽 공백 문자를 제거한다.
'''
s = " 상하좌우 "
print(s.strip())
print(s.lstrip())
print(s.rstrip())

'''
문자열 분할, 결합, 교체
    split() : 문자열에서 특정 문자(공백, 콤마) 등을 기준으로 분할한다.
    join() : 모든 문자열을 특정 문자로 결합한다.
    replace() : 특정 문자를 다른 문자로 변경한다.
'''
s1 = "Hello python!"
print(s1.split())   # 공백을 기준으로 문자열을 분할
s2 = "Good morning, python!"
print(s2.split(','))

s = "동서남북"
print(",".join(s))  # 각 글자 사이에 콤마(,)를 넣음

s = "Good Day!"
print(s.replace("Good", "Beautiful"))   # 특정 문자열을 찾아 다른 문자열로 교체

'''
문자열 정렬
    center() : 문자열을 특정 폭에 맞추어 가운데 정렬
    ljust() : 문자열을 특정 폭에 맞추어 왼쪽 정렬
    rjust() : 문자열을 특정 폭에 맞추어 오른쪽 정렬
    zfill() : 문자열의 빈자리를 0으로 채운다
'''
s = "Hi"
print(s.center(10))     # 문자열 폭 10, 문자 가운데 정렬
print(s.ljust(10))      # 문자열 폭 10, 문자 왼쪽 정렬
print(s.rjust(10))      # 문자열 폭 10, 문자 오른쪽 정렬
print(s.zfill(10))      # 문자열 폭 10, 빈자리 0으로 채움

'''
자료형 변환

    input() 함수를 이용해 입력받은 값은 모두 문자열
    숫자로 인식되게 하기 위해 변환이 필요하다.
'''
num = input("좋아하는 숫자를 입력하세요 : ")
k = int(num)
print(type(k))

num = int(input("좋아하는 숫자를 입력하세요 : "))
print(type(num))