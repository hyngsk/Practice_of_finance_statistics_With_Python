# %%[과제8-1] 서울 기온 데이터에서 기상 관측 이래 일교차가 가장 컸던 날은 언제인지
# 찾고, 다음과 같이 출력하시오.
# 출력: '기상 관측 이래 서울의 일교차가 가장 컸던 날은 yyyy-mm-dd로 일교차는 xx 였습니다.'


import csv

f = open('seoul.csv', 'r', encoding='cp949')

data = csv.reader(f, delimiter=',')
header = next(data)

# noinspection NonAsciiCharacters
일교차 = -999  # 일교차 담을 공갈 변수
date = ''  # 이교차가 최대인 날짜를 담을 변수

for row in data:
    if row[-1] == '' or row[-2] == '':  # 최고기온이나 최저기온이 존재하지 않으면
        row[-1] = -999  # 임의의 값 설정
        row[-2] = -999
    else:  # 존재하면 형 변환
        row[-1] = float(row[-1])
        row[-2] = float(row[-2])

    if row[-1] - row[-2] > 일교차:  # 최고기온 - 최저기온이 탐색한 일교차 보다 크다면
        일교차 = float(row[-1] - row[-2])  # 일교차와
        date = row[0]  # 날짜 저장
f.close()

print('기상 관측 이래 서울의 일교차가 가장 컸던 날은', date + '로 일교차는 ', 일교차, ' 였습니다.')
