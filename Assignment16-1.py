# %% [과제16-1] 'gender.csv'파일을 사용해서 관심있는 지역을 선택한 후 그 지역의
# 남자와 여자 각 연령대별 인구구성비를
# 따로 구하고 (예, 남자 0세 인구구성비=남자0세 인구/남자 총인구,
# 여자 0세 인구구성비=여자 0세 인구수/여자 총인구),
# 그 지역과 남자와 여자 인구구성비가 가장 비슷한 지역을 찾아서 시각화 하시오.
# 시각화 방법은 여러분이 편한 방법(시각화가 가장 훌륭한 방법)을 선택하세요.
# 가장 비슷한 지역을 찾는 방법:
# np.sum((maleHome-male_away)**2+(femaleHome-female_away)**2)
import csv
import matplotlib.pyplot as plt
import numpy as np

f = open('gender.csv')
data = csv.reader(f)
next(data)
data = list(data)
homeName = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
awayName = ''  # 결과 지역 이름
maleHome, maleAway, femaleHome, femaleAway = [], [], [], []  # 남자, 여자 결과 데이터
minSimilarity = 0  # 최소 유사도
# similarity = [] # 유사도 확인 리스트
for row in data:
    temp = []
    if homeName in row[0]:
        for i in row[2:]:
            temp.append(i.replace(',', ''))
        # get male, female data about input location
        maleHome = np.array(temp[1:102], dtype=int) / int(temp[0]) * 100
        femaleHome = np.array(temp[104:], dtype=int) / int(temp[102]) * 100
for row in data:
    temp = []
    for i in row[2:]:
        temp.append(i.replace(',', ''))
    # searching
    compareM = np.array(temp[1:102], dtype=int) / int(temp[0]) * 100
    compareF = np.array(temp[104:], dtype=int) / int(temp[102]) * 100
    # calculate Similarity. (Similarity has range of 0 < S < 1)
    Similarity = (1 / (1 + np.sqrt(np.sum((maleHome - compareM) ** 2 + (femaleHome - compareF) ** 2))))
    # similarity.append(Similarity)
    if Similarity == 1 and homeName not in row[0]:  # if Away has same value in the data
        minSimilarity = Similarity  # capture the similarity
        awayName = row[0]  # capture the name
        maleAway = compareM  # capture the male value of the comparing row
        femaleAway = compareF  # capture the female value of the comparing row
    elif minSimilarity < Similarity and homeName not in row[0]:  # maximum similarity updated to 'minSimilarity'
        minSimilarity = Similarity  # capture the similarity
        awayName = row[0]  # capture the name
        maleAway = compareM  # capture the male value of the comparing row
        femaleAway = compareF  # capture the female value of the comparing row
# 유사도 확인
# print(similarity, minSimilarity)
print('유클리디안 유사도 :', float(minSimilarity * 100), '%')
plt.figure(dpi=150)
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.subplot(211)
plt.title(homeName + ' 지역과 가장 비슷한 인구 구조를 가진 지역')
plt.plot(maleHome, label=homeName + "남자")
plt.plot(maleAway, label=awayName + "남자")
plt.ylabel('연령대 별 인구 구성비(%)')
plt.legend(loc='upper right', fontsize='xx-small')

plt.subplot(212)
plt.plot(femaleHome, label=homeName + "여자")
plt.plot(femaleAway, label=awayName + "여자")
plt.ylabel('연령대 별 인구 구성비(%)')
plt.xlabel('연령(세)')
plt.legend(loc='upper right', fontsize='xx-small')
plt.show()
