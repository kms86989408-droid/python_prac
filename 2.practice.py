# 나도코딩 
# https://youtu.be/kWiCuklohdY?si=n7s67g3gv82gSBSG

# ======= 2-4 변수 =======
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

# ======= 3-1 연산자 =======
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


# =======3-3 숫자 처리 함수=======
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

# =======3-4 랜덤 함수=======
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

# =======4-1 문자열=======
# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고
# 파이썬은 쉬워요"""
# print(sentence3)

# =======4-2 슬라이싱=======
# jumin = "123456-1234567"

# print("성별 : " +jumin[7])
# print("연생 : "+jumin[0:2]) # 0 부터 2 직전까지(0,1)
# print("월 : "+jumin[2:4])
# print("일 : "+jumin[4:6])
# print("생년월일 : " +jumin[:6]) # 처음부터 6직전까지
# print("뒤 7자리 : "+jumin[7:]) # 7 부터 끝까지
# print("뒤 7자리(뒤에서부터) : "+jumin[-7:]) # 맨뒤에서 7번째부터 끝까지


# =======4-3 문자열 처리 함수=======
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


# =======4-4 문자열 포맷=======
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


# =======4-5 탈출 문자=======
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

# site = "http://naver.com"
# my_str = site.replace("http://","") # 규칙1
# my_str = my_str[:my_str.index(".")] # 규칙2
# my_str[0:5] -> 0 ~ 5 직전까지
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는 {1}입니다.".format(site, password))

# =======5-1 리스트[] =======

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]

# subway = ["유재석, 조세호, 박명수"]
# # 조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))
# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하") # append는 맨 뒤에 추가됨
# print(subway)
# # 정현돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)
# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop()) # 뒤에서부터 객체를 제거함
# print(subway)

# 같은 이름의 사람이 몇명인지 확인하기
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# 정렬
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기 가능
# num.list.reverse()

# # 모두 지우기
# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20 ,True]
# print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# =======5-2 사전 =======
# cabinet = {3 : "유재석", 100:"김태호"}
# print(cabinet[3]) # 해당하는 키가없을경우 프로그램 종료
# print(cabinet.get(3)) # 해당하는 키가 없을경우 None 출력 프로그램 진행
# print(cabinet.get(5, "사용 가능")) # None 대신 "사용가능" 출력

# print(3 in cabinet) # True
# print(5 in cabinet) # False

# cabinet ={"A-3" : "유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# # 새손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# # 간 손님
# del cabinet["A-3"]
# print(cabinet)
# # key 들만 출력
# print(cabinet.keys())
# # value 들만 출력
# print(cabinet.values())
# # key, value 쌍으로 출력
# print(cabinet.items())
# # 목욕탕 폐점 
# cabinet.clear()
# print(cabinet)

# =======5-3 튜플 =======
# menu = ("돈까스","치즈가스")
# print(menu[0])
# print(menu[1])

# # menu.add("생선까스") # 추가 불가능
# name = "김종국"
# age = "20"
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

# =======5-4 SET(집합) =======
# # 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3,3}
# print(my_set) # 3은 하나만 출력됨

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])
# # 교집합 (java와 python을 모두 할수 있는 개발자)
# print(java & python)
# print(java.intersection(python))
# # 합집합(java도 할 수 있거나 python 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))
# # 차집합(java는 할 수 있지만 python은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))
# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)
# # java를 잊어버림
# java.remove("김태호")
# print(java)

# =======5-5 자료구조의 변경 =======
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# Quiz) 당신의 학교에서는 파이썬 코딩대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
# 댓글 작성자중 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받는다

# 1. 편의상 댓글은 20명이 작성하였고 ID는 1~20으로 가정
# 2. 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 3. random 모듈의 shuffle과 sample을 활용
# 출력 예제
# --- 당첨자 발표 ---
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# --- 축하합니다 ---
# 활용 예제
# from random import*
# users = range(1, 21)
# # print(type(users))
# users = list(users)
# # print(type(users))

# # print(users)
# shuffle(users)
# # print(users)
# winners = sample(users, 4)
# # print(winners)
# print("--- 당첨자 발표 ---")
# print("치킨 당첨자 : {0}" .format(winners[0]))
# print("커피 당첨자 : {0}" .format(winners[1:]))
# print("--- 축하합니다 ---")

# =======6-1 If =======
# weather = input("오늘 날씨는 어때요?")
# # if 조건:
# #     실행 명령문
# if weather =="비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요없어요")

# temp = int(input("기온은 어떄요?"))
# if 30 <= temp:
#     print("너무 더워요. 나가지마세요")
# elif 10<= temp and temp <30 :
#     print("괜찮은 날씨에요")
# elif 0<= temp < 10 :
#     print("외투를 챙기세요")
# else :
#     print("너무 추워요. 나가지마세요")

# =======6-2 for =======
# for watting_num in range(1, 6): # 1, 2, 3, 4, 5
#     print("대기번호 : {0}".format(watting_num))

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks :
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# =======6-3 while =======
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index =1
# while Ture :
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index +=  # 무한루프됨

# customer = "토르"
# person = "Unknown"
# while person != customer : # 조건이 만족할때 까지 반복
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

# =======6-4 continue, break =======
# absent = [2, 5] # 결석
# no_book = [7] # 책을 깜박함
# for student in rang(1, 11): # 1 ~ 10
#     if student in absent : # student 내에 absent가 포함되있다면 건너뛰기
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

# =======6-5 한줄 for문 활용 =======
# # 출석 번호가 1 2 3 4 앞에 100을 붙이기로함 -> 101 102 103 104
# student = [1,2,3,4,5]
# student = [i+100 for i in student]
# print(student)

# # 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "groot"]
# students = [len(i) for i in students]
# print(student)

# # 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "groot"]
# students = [i.upper() for i in students]
# print(students)

# Quiz) 당신은 cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을떄, 총 탑승 승객 수를 구하는 프로그램을 작성하시오
# 1. 승객별 운행 소요 시간은 5 ~ 50분 사이의 난수로 정해집니다.
# 2. 당신은 소요시간 5 ~ 15분 사이의 승객만 매칭해야합니다.

# 출력문 예제
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)
# 총 탑승 승객 : 2명

# from random import*
# 내가한거
# time = list(range(5,51))
# for customers in range(1, 51):
#     ran_time = sample(time, 1)[0]
#     if 5 <= ran_time <= 15:
#         check = "O"
#         count = 0
#         count += 1
#     else :
#         check = " "
#     print("[{0}] {1}번째 손님 (소요 시간 : {2})".format(check, customers, ran_time))

# print("총 탑승승객 : {0} 분".format(count)) 

# 강의 해석
# cnt = 0 # 총 탑승 승객
# for i in range(1, 51): # 1 ~ 50 이라는수 ( 승객)
#     time = randrange(5, 51) # 5분 ~ 50분 소요시간
#     if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님, 탑승 승객 수 증가 처리
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt +=1
#     else:
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

# print("총 탑승 승객 : {0} 분".format(cnt))

# =======7-1 함수 =======
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
# open_account()

# def deposit(balance, money): # 입금
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
#     return balance+money
# def withdraw(balance, money): # 출금
#     if balance >= money: # 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
#         return balance-money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
#         return balance
# def withdraw_night(balance, money): # 저녁에 출금 수수료 발생
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commission

# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))

# =======7-3 기본값 =======
# def profile(name, age, main_lang):
#     print("이름 : {0}\t 나이: {1}\t주 사용언어{2}".format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# # 같은 학교 같은 학년 같은 반 같은 수업
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t 나이: {1}\t주 사용언어{2}"\
#           .format(name, age, main_lang))
# profile("유재석")
# profile("김태호")

# =======7-4 키워드 값 =======
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)

# =======7-5 가변인자 =======
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)
# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language :
#           print(lang, end= " ")
#     print()

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift","", "", "")

# =======7-6 지역변수와 전역변수 =======
# gun = 10

# def checkpoint(soldiers): # 경계근무
#     global gun #전역 공간에 있는 gun 사용 (가급적 사용x)
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun
# print("전체 총 :{0}".format(gun))
# # checkpoint(2)
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

# Quiz) 표준 체중을 구하는 프로그램을 작성하시오
# * 표준 체중 : 각 개인의 키에 적당한 체중
# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 1) 표준 체중은 별도의 함수 내에서 계산
#     * 함수명 : std_weight
#     * 전달값 : 키(height), 성별(gender)
# 2) 표준 체중은 소수점 둘째자리까지 표시
# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

# def std_weight(height, gender):
#     if gender == "남자":
#         i = 22
#     elif gender == "여자":
#         i = 21
#     return height*height*i

# height = 175 # cm 단위
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm {1}의 표준체중은 {2}kg 입니다.".format(height,gender, weight))

# =======8-1 표준 입출력 =======
# print("Python", "Java", sep=",", end="?")
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout) #stdout 표준출력
# print("Python", "Java", file=sys.stderr) #stderr 표준에러

# 시험 성적
# scores ={"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score.rjust(4)), sep=":") 
#     #ljust(8)왼쪽 정렬 8개의 공간 확보, rjust(4) 4칸의 공간확보 오른정렬

# 은행 대기 순번표
# 001, 002, 003, 004 .....
# for num in range(1, 21):
#     print("대기번호 :" + str(num).zfill(3)) 
#     # 3크기만큼의 공간 확보 값이없는 빈공간 0으로 채우기

# 표준 입력
# answer = input("아무값이나 입력하세요 :") # input으로 받으면 type = 문자열
# print( "입력하신값은" +answer+ "입니다.")

# =======8-2 다양한 출력포맷 =======
# # 빈자리는 빈공간으로 두고, 오른쪽 정렬을하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸을 _로 채움
# print("{0:_<+10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(100000000))
# # 3자리 마다 콤마를 찍어주기, +-부호도 붙이기
# print("{0:+,}".format(100000000))
# # 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보
# # 빈자리는 ^ 로 채우기
# print("{0:^<+30,}".format(100000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수까지만 표시 (소수점 3번째에서 반올림)
# print("{0:.2f}".format(5/3))

# =======8-3 파일입출력 =======
# score_file = open("score.txt", "w", encoding="utf8") # 'w'는 write 쓰기
# print("수학 : 0",file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")  # 'a'는 append 이어쓰기
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # 'r'는 read 읽어오기
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline()) 
# print(score_file.readline()) 
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True :
#     line = score_file.readline()
#     if not line :
#         break
#     print(line, end="") #end로 줄바꿈없앰
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines :
#     print(line, end="")

# score_file.close()

# =======8-4  pickle =======
# import pickle
# profile_file = open("profile.pickle", "wb") # b는 binary pickle에서 필수! pickle에서 encoding은 하지않아도됨
# profile = {"이름" : "박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# =======8-5 with =======
# import pickle

# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬 공부중입니다.")
# with open("study.txt", "r",encoding="utf8") as study_file:
#     print(study_file.read())

# Quiz) 당신은 회사에서 매주 1회 작성해야하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야합니다.

# - X 주차 주간 보고 -
# 부서 : 
# 이름 : 
# 업무 요약 :
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오
# 조건 : 파일명은 '1주차.txt'와 같이 만든다.

# def report():
#     for i in range(1,51):
#         with open("{0}주차.txt".format(i), "w", encoding="utf8") as w_report:
#             w_report.write("- {0} 주차 주간보고 - \n부서 : \n이름 : \n업무 요약 :".format(i))
#         print(type(i))
# report()

# =======9-1 클래스 9-2 init 9-3 멤버 변수 9-4 매소드 9-5 상속 =======
# =======9-6 다중상속 9-7 매소드 오버라이딩 9-8 Pass 9-9 Super =======
# from random import *

# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print(f"{name} 유니싱 생성되었습니다.")

#     def move(self, location) :
#         print("[지상 유닛 이동]")
#         print(f"{self.name} : {location}방향으로 이동합니다. [속도 {self.speed}]")

#     def damaged(self, damage):
#         print(f"{self.name} : {damage} 데미지를 입었습니다.")
#         self.hp -= damage
#         print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
#         if self.hp <= 0:
#             print(f"{self.name} : 파괴되었습니다.")

# # # marine1 = Unit("마린", 40, 5)
# # # marine2 = Unit("마린", 40, 5)
# # # tank = Unit("탱크", 150, 35)
# # # 레이스 : 공중유닛, 비행기. 클로킹
# # wraith1 = Unit("레이스", 80, 5)
# # print(f"유닛 이름 : {wraith1.name}, 공격력 {wraith1.damage}")

# # # 마인드 컨트롤
# # wraith2 = Unit("뺴앗은 레이스", 80, 5)
# # wraith2.clocking = True
# # # 클래스 외부에서 객체에 확장 가능
# # if wraith2.clocking == True:
# #     print(f"{wraith2.name} 은 현재 클로킹 상태입니다.")

# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed ,damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
#     def attack(self, location):
#         print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")

#     # def damaged(self, damage):
#     #     print(f"{self.name} : {damage} 데미지를 입었습니다.")
#     #     self.hp -= damage
#     #     print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
#     #     if self.hp <= 0:
#     #         print(f"{self.name} : 파괴되었습니다.")

# class Flyable : 
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#     def fly(self, name, location):
#         print(f"{name} : {location} 방향으로 날아갑니다. 속도 {self.flying_speed}")

# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# # # 건물 
# # class uildingUnit(Unit):
# #     def __init__(self, name, hp, location):
# #         #Unit.__init__(self, name, hp, 0)
# #         super().__init__(name, hp, 0)
# #         self.location = location

# # 마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)
#     # 스팀팩
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print(f"{self.name} : 스팀팩을 사용합니다(hp10감소)")
#         else:
#             print(f"{self.name} : 체력이 부족하여 스팀팩을 사용하지 않습니다.")
# # 탱크
# class Tank(AttackUnit):
#     # 시즈모드
#     seize_developed = False #시즈모드 개발여부
#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.set_seize_mode = False
    
#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return
#         # 현재 시즈모드가 아닐 떄 -> 시즈모드
#         if self.seize_mode == False:
#             print(f"{self.name} : 시즈모드로 전환합니다.")
#             self.damage *= 2
#             self.seize_mode = True
#         # 현재 시즈모드 일 때 -> 시즈모드 해제
#         else:
#             print(f"{self.name} : 시즈모드로 해제합니다.")
#             self.damage /= 2
#             self.seize_mode = False
# # 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False

#     def clocking(self):
#         if self.clocked == True: #클로킹모드 -> 모드해제
#             print(f"{self.name} : 클로킹 모드 해제합니다.")
#             self.clocked = False
#         else:
#             print(f"{self.name} : 클로킹 모드 설정합니다.")
#             self.clocked = True

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("Player : gg")
#     print("[Player] 님이 게임에서 퇴장하셨습니다,")

# # 게임 시작
# game_start()
# # 마린 3기 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()
# # 탱크 2기 생성
# t1 = Tank()
# t2 = Tank()
# # 레이스 1기 생성
# w1 = Wraith()

# # 유닛 일괄 관리 (생성된 모든 유닛 append)
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")
# # 탱크 시즈모드 개발
# Tank.seize_developed = True
# print("[알림] 탱크 시즈모드 개발 완료")

# # 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()
# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# # 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5, 21)) # 공격은 랜덤으로 받음 (5~20)

# # 게임 종료
# game_over

# # # 발키리
# # valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# # valkyrie.fly(valkyrie.name, "3시")
# # # 파이어뱃
# # firebat1 = AttackUnit("파이어뱃", 50, 16)
# # firebat1.attack("5시")
# # # 벌쳐
# # vulture = AttackUnit("벌쳐", 80, 10, 20)
# # # 배틀 크루저
# # battlecrusier = FlyableAttackUnit("배틀크루져", 500, 25, 3)

# # vulture.move("11시")
# # battlecrusier.move("9시")
# # #공격 2번 받는다고 가정
# # firebat1.damaged(25)
# # firebat1.damaged(25)

# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.
# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     # 매물 정보 표시
#     def show_detail(self):
#         print(f"{self.location}, {self.house_type}, {self.deal_type}, {self.price}, {self.completion_year}")

# houses = []
# house1 = House("강남","아파트","매매","10억","2010년")
# house2 = House("마포","오피스텔","전세","5억","2007년")
# house3 = House("송파","빌라","월세","500/50","2000년")
# houses.append(house1)
# houses.append(house2)
# houses.append(house3)

# print(f"총 {len(houses)}대의 매물이 있습니다.")
# for house in houses:
#     house.show_detail()


# ======= 10-1 예외 처리 =======
# try:
#     print("나누기 전용 계산기 입니다.")
#     nums =[]
#     nums.append(int(input("첫 번째 숫자를 입력하세요 :")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 :")))
#     # nums.append(int(nums[0] / nums[1])) # 이 줄을 빼먹었다면
#     print(f"{nums[0]} / {nums[1]} = {nums[2]}")
# except ValueError:
#     print("에러! 잘못된 값이 입력되었습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except: # 이 줄을 빼먹었을때 'Exception as err' 처리하면 리스트 에러 확인가능
#     print("알 수 없는 에러가 발생하였습니다.") #(나머지 모든 에러 여기서 처리)

# ======= 10-2 에러발생 시키기, 10-3 사용자 정의 예외처리, 10-4 Finally =======
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 :"))
#     num2 = int(input("두 번째 숫자를 입력하세요 :"))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError(f"입력값 : {num1}, {num2}")
#     print(f"{num1} / {num2} = {int(num1/num2)}")
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
# except BigNumberError as err:
#     print("에러가 발생했습니다. 한자리만 입력하세요.")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")

# Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오

# 1) 1보다 작거나 숫자가 아닌 입력값이 들어올떄는 ValueError로 처리
#     출력 메세지 : "잘못된 값을 입력하였습니다"
# 2) 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#     치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#     출력 메세지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

# class SoldOutError(Exception):
#     pass
# chicken = 10
# waiting = 1 # 홀은 만석  대기번호 1부터 시작
# while(True):
#     try:
#         print(f"[남은치킨] : {chicken}")
#         order = int(input("치킨 몇마리 주문하시겠습니까?"))
#         if order > chicken:
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print(f"[대기번호 {waiting} {order} 마리 주문 되었습니다.]")
#         waiting += 1
#         chicken -= order
#         if chicken == 0:
#             raise SoldOutError
#     except ValueError:
#         print("잘못된 값을 입력하였습니다")
#     except SoldOutError:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break

# ======= 11-1 모듈 =======
# import theater_module
# theater_module.price(3) # 3명이 영화 보러갔을때 가격
# theater_module.price_morning(4) # 4명이 조조할인
# theater_module.price_soldier(5) # 5명의 군인

# import theater_module as mv # theater_module 을 mv로 호출 가능 
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(3)
# price_morning(4)
# price_soldier(5) # price와 price_morning 만 import해서 오류가 생김

# from theater_module import price_soldier as s_price
# s_price(5)

# ======= 11-2 패키지 =======
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# ======= 11-3 All 11-4 모듈 직접 실행 =======
# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# ======= 11-5 패키지, 모듈 위치 =======
# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

# ======= 11-6 pip install =======
# google -> pypi
# python -m pip install beautifulsoup4
# from bs4 import BeautifulSoup

# ======= 11-7 내장 함수 =======
# google -> list of python builtins
# input : 사용자 입력 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print(f"{language}는 아주 좋은 언어입니다!")

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 함수를 가지는지 표시
# print(dir())
# import random # 외장 함수
# print(dir())
# import pickle # 외장 함수
# print(dir())
# print(dir(random)) # 랜덤 함수에서 쓸 수 있는 내용

# ======= 11-8 외장 함수 =======
# google -> list of python modules
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더 입니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print(datetime.date.today())

# # timedelta : 두 날짜 사이의 간격
# today = datetime.date.today() #오늘 날짜 지정
# td = datetime.timedelta(days=100) # 100일 저장
# print("100일째 되는날은",today + td)

# Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오
# 1) 모듈 파일명은 byme.py로 작성
# [사용 모듈]
import byme
byme.sign()
# [출력 예제]
# 이 프로그램은 나도 코딩에 의해 만들어졌습니다.
# 유튜브 : http://youtube.com
# 이메일 : 1111@gmail.com