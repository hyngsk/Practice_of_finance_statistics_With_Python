# %%[과제10-1] 기온데이터에서 일교차를 모두 구하고 월별로 일교차를 보여주는 Boxplot을 그리시오.
import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
header = next(data)
Month = {'01': [], '02': [], '03': [], '04': [], '05': [], '06': [],
         '07': [], '08': [], '09': [], '10': [], '11': [], '12': []}

for row in data:
    if row[-1] != '':
        Month[row[0].split('-')[1]].append(float(row[-1]) - float(row[-2]))
f.close()

plt.figure(figsize=(10, 5))
plt.rc('font', family='Malgun Gothic')  # 맑은 고딕을 기본 글꼴로 설정
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지
plt.boxplot(Month.values())
plt.title('월별 일교차')
plt.xlabel('월')
plt.ylabel('기온')
plt.show()  # 그래프 나타내기
