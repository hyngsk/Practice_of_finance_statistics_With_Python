# %% [과제12-1] 인터넷에서 'matplotlib bar'를 검색해서 막대그래프의 색을 변경하는
# 방법을 검색하고 원하는 색으로 변경하는 코드를 작성해서 제출하세요.
import csv
import matplotlib.pyplot as plt

f = open('age.csv')
data = csv.reader(f)
result = []
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요: ')
for row in data:
    if name in row[0]:
        for i in row[3:]:
            result.append(int(i.replace(',', '')))

plt.bar(range(101), result, color='cyan')  # bar(막대를 표시할 위치, 막대의 높이)


plt.show()
