# %% [과제12-2] [과제12-2]결과와 동일한 결과를 생성하는 코드를 작성하세요.

import csv
import matplotlib.pyplot as plt

f = open('gender.csv')
data = csv.reader(f)

# initialization
resultOfLoc1 = []
resultOfLoc2 = []

# 입력
locInput1 = input("인구 구조를 비교하고 싶은 첫번째 지역의 이름(읍면동 단위)을 입력해주세요: ")
genInput1 = input("인구 구조를 비교하고 싶은 첫번째 지역의 성별을 입력하세요(예: 남 또는 여): ")
locInput2 = input("인구 구조를 비교하고 싶은 두번째 지역의 이름(읍면동 단위)을 입력해주세요: ")
genInput2 = input("인구 구조를 비교하고 싶은 두번째 지역의 성별을 입력하세요(예: 남 또는 여): ")

# Search
for row in data:
    # Take data for the left part of graph
    if locInput1 in row[0]:
        if genInput1 == '남':
            genInput1 = '남자'  # 표기 변경
            for i in row[3:104]:
                resultOfLoc1.append(-int(i))
        else:  # 여
            genInput1 = '여자'  # 표기 변경
            for i in row[106:]:
                resultOfLoc1.append(-int(i))

    # Take data for the right part of graph
    if locInput2 in row[0]:
        if genInput2 == '남':
            genInput2 = '남자'  # 표기 변경
            for i in row[3:104]:
                resultOfLoc2.append(int(i))
        else:  # 여
            genInput2 = '여자'
            for i in row[106:]:
                resultOfLoc2.append(int(i))

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title(str(locInput1) + '과 ' + str(locInput2) + ' 지역의 인구 분포')
plt.barh(range(101), resultOfLoc1, label=str(locInput1 + ' ' + genInput1))
plt.barh(range(101), resultOfLoc2, label=str(locInput2 + ' ' + genInput2))
plt.xticks([-300, -200, -100, 0, 100, 200, 300], [300, 200, 100, 0, 100, 200, 300])
plt.legend()
plt.show()
