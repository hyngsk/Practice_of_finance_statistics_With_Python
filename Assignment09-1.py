# %% [과제9-1] 일교차를 계산하여 저장할 리스트를 생성하고 1983년 이후 8월 15일의 일교차를
# 그래프로 그리시오.
import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
header = next(data)
DailyTempRange = []  # 일교차 담을 공갈 변수
Year = []
for row in data:
    if row[-1] != '' and row[-2] != '':
        if int(row[0].split('-')[0]) >= 1983:
            if row[0].split('-')[1] == '08' and row[0].split('-')[2] == '15':
                DailyTempRange.append(float(row[-1]) - float(row[-2]))  # 일교차 저장
                Year.append(int(row[0].split('-')[0]))  # 년도 저장
f.close()

plt.figure(1, figsize=[13, 4], dpi=100)
plt.rc('font', family='Malgun Gothic')  # 맑은 고딕을 기본 글꼴로 설정
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지
plt.title('1983년이후 년도별 광복절 기온차')  # 제목 설정
x = Year
y = DailyTempRange
plt.plot(x, y, 'skyblue', label='일교차')
plt.xlabel("년도")
plt.ylim(0, 20)
plt.ylabel("온도")
plt.legend()  # 범례 표시
plt.show()  # 그래프 나타내기
