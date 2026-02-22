# ======= 변수 =======
# 애완동물을 소개해주세요
# name = "연탄이"
# animal = "강아지"
# age = 4
# hobby = "산책"
# is_adult = age >= 3

# print("우리집 "+ animal +"의 이름은 "+ name +"이에요")
# hobby = "공놀이"
# print(name,"는" ,age, "살이며," ,hobby,"을 좋아해요")
# print("연탄이는 어른일까요? "+ str(is_adult) +"")

# Quiz) 변수를 이용하여 다음 문장을 출력하시오
# 변수명 : station
# 변수값 : 사당, 신도림, 인천공항
# 출력 문장 : XX 행 열차가 들어오고 있습니다.

# station = "사당"

# print(station +"행 열차가 들어오고있습니다.")

# ======= 연산자 =======
# print(1+1) # 2
# print(3-2) # 1
# print(5*2) # 10
# print(6/3) # 2

# print(2**3) # 2^3 = 8
# print(5%3) # 나머지 구하기 2
# print(10%3) # 1
# print(5//3) # 몫 1
# print(10//3) # 몫 3

# print(10 > 3) # True
# print(4 >= 7) # False
# print(10 < 3) # False
# print(5 <= 5) # True

# print(3 == 3) # True
# print(4 == 2) # False
# print(3 + 4 == 7) # True

# print(1 != 3) # NOT -> True
# print(not(1 != 3)) # False

# print((3 > 0) and (3 < 5)) # True
# print((3 > 0) & (3 < 5)) # AND -> True

# print((3 > 0) or (3 > 5)) # True
# print((3 > 0) | (3 > 5)) # OR -> True

# print(5 > 4 > 3) # True
# print(5 > 4 > 7) # False


# =======숫자 처리 함수=======
# print(abs(-5)) # abs절대값 # 5
# print(pow(4, 2)) # 4^2 = 4*4 = 16
# print(max(5, 12)) # 최대값 출력 # 12
# print(min(5, 12)) # 최소값 출력 # 5
# print(round(3.14)) # 반올림 # 3
# print(round(4.99)) # 반올림 # 5

# from math import * # math 라이브러리 모든것 사용
# print(floor(4.99)) # 소수점 내림 # 4
# print(ceil(3.14)) # 소수점 올림 # 4
# print(sqrt(16)) # 제곱근 # 4

# =======랜덤 함수=======
# from random import *

# print(random()) # 0.0 이상 1.0 미만의 임의의값 생성
# print(random() * 10) # 0.0 ~ 10.0 미만의 값 생성
# print(int(random()*10)) # 0 ~ 10 미만의 값 생성
# print(int(random()*10)+1) # 1 ~ 10 이하의 값 생성

# print(int(random()*45)+1) # 1 ~ 45 이하의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

# Quiz) 당신은 최근에 코딩 스터디 모임을 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로하고 1번은 오프라인으로 함
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주시오

# 1. 랜덤으로 날짜를 뽑아야함
# 2. 월별 날짜는 다름을 감안하여 최소 일수인 28이내로 정함 
# 조건 매월 1~3일은 스터디 준비를 해야하므로 제외
# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x일 로 선정되엇습니다.

# date = (randint(4, 28))
# print("오프라인 스터디 모임 날짜는 매월 "+str(date)+"일로 선정되었습니다.")

# =======문자열=======
# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고
# 파이썬은 쉬워요"""
# print(sentence3)

# =======슬라이싱=======
# jumin = "123456-1234567"

# print("성별 : " +jumin[7])
# print("연생 : "+jumin[0:2]) # 0 부터 2 직전까지(0,1)
# print("월 : "+jumin[2:4])
# print("일 : "+jumin[4:6])
# print("생년월일 : " +jumin[:6]) # 처음부터 6직전까지
# print("뒤 7자리 : "+jumin[7:]) # 7 부터 끝까지
# print("뒤 7자리(뒤에서부터) : "+jumin[-7:]) # 맨뒤에서 7번째부터 끝까지


# =======문자열 처리 함수=======
# python = "Python is Amazing"
# print(python.lower()) # 소문자 변환
# print(python.upper()) # 대문자 변환
# print(python[0].isupper()) # 첫번째 글짜가 대문자인지 확인
# print(len(python)) # 문자열의 길이
# print(python.replace("Python", "Java")) # Python을 Java로 변환

# index = python.index("n") # 'n' 이 몇번째 위치하는지
# print(index) # 5
# index = python.index("n", index + 1) # 두번째 'n' 위치
# print(index) # 15

# print(python.find("n")) # 'n' 위치를 찾기
# print(python.find("Java")) # 글자가 없을때 -1 출력(프로그램 진행)
# print(python.index("Java")) # 글자가 없을때 오류 프로그램종료

# print(python.count("n")) # 'n'이 몇개 있는지


# =======문자열 포맷=======
# print("a" + "b")
# print("a", "b")

# 방법 1
# print("나는 %d살 입니다."%20) # %d 는 정수값
# print("나는 %s을 좋아해요" %"파이썬") # %s는 문자열
# print("Apple은 %c로 시작해요" %"A") # %c는 문자
# # %s
# print("나는 %s살 입니다."%20)
# print("나는 %s색과 %s색을 좋아해요" %("파란", "빨강"))

# 방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요" .format("파란","빨강"))
# print("나는 {1}색과 {0}색을 좋아해요" .format("파란","빨강"))

# 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age =20, color="빨강"))

# 방법 4 (ver. 3.6이상 ~)
# age = 20
# color = "빨강"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")


# =======탈출 문자=======
# \n : 줄바꿈
# print("백문이 불여일견\n백견이 불여일타")
# \"\" 문장 내에서 따옴표
# ex) 저는 "나도코딩"입니다.
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")

# \\ : 문장내에서 \
# print(" C:\\Users\\kms86\\Desktop\\coding\\python_prac>")

# \r :커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# \b : 백스페이스(한 글자 삭제)
# print("redd\bApple")

# \t : Tap
# print("Red\tApple")

# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램
# ex) http://naver.com
# 1. http:// 부분은 제외 -> naver.com
# 2. 처음 만나는 점(.) 이후 부분은 제외 -> naver
# 3. 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

site = "http://naver.com"
my_str = site.replace("http://","") # 규칙1
my_str = my_str[:my_str.index(".")] # 규칙2
# my_str[0:5] -> 0 ~ 5 직전까지
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(site, password))