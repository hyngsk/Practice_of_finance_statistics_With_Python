# datetime 패키지의 date 만 사용
from datetime import date

# 현재날짜를 받아오는 함수 date.today()에서 년도만 추출해 정수형 저장
currentYear = int("{:%Y}".format(date.today()))

# 입력
name = input("이름을 입력하세요. : ")
age = int(input("나이를 입력하세요. : "))

# 출생년도 계산
birthYear = currentYear - age + 1

# 출력
print(name, "님의 출생 년도는 ", birthYear, "년 입니다. ")

# datetime 사용법 출처 https://m.blog.naver.com/dudwo567890/130165166038
