"""
- 개인 프로젝트 수행 요청
   * 본인이 알고자 (연구하고자) 하는 주제를 선정한 후
   * 관련된 데이터를 선택하여 수집하고
   * 데이터로 부터 본인이 연구하고자 하는 문제에 대한 해답을 찾고
   * 연구한 결과를 가장 잘 나타낼 수 있는 시각화 방법을 사용하여 시각화
   * 시각화한 자료를 바탕으로 간략한 보고서와 발표 영상을 제작하여 제출

 - 제출자료
   * 간략한 보고서: 한글 보고서 3페이지 이상 ~ 5페이지 이내
        => 학과_학번_이름_보고서.hwp로 제출, 예) 국제금융학과_20180654_홍길동_보고서.hwp
        => 글자크기 11
   * 간략한 발표자료: 파워포인트 10페이지 이상 ~ 15페이지 이내
        => 학과_학번_이름_발표자료.ppt로 제출, 예) 국제금융학과_20180654_홍길동_발표자료.ppt
   * 발표 동영상: 15분 이내 발표자료
        => 학과_학번_이름_발표영상.mp4로 제출, 예) 국제금융학과_20180654_홍길동_발표영상.mp4

- 제출기한: 6월 26일 (금)
- 제출방법: 추후 제출 링크 따로 제공

- 발표 동영상 제작 기준
   * 발표 동영상은 제가 수업을 했던 것과 비슷하게 컴퓨터화면을 녹화하고 음성을 입혀서 발표
- 평가기준
   * 1명의 학생은 다른 5명의 학생의 보고서, 발표자료, 발표영상을 보고 발표한 5명의 학생에게 1~5점의 점수중 하나를 부여함
   * 점수 부여시 1~5점을 한번씩만 부여할 수 있음. 즉, 5명의 발표학생에게 각기 다른 점수를 1~5점에서 선택하여 부여
   * 발표한 학생은 5명의 학생으로 부터  5개의 점수를 받게 되고, 5개의 점수중에서
   최고점수와 최저점수는 제외하여 3개의 점수를 받음. 예) 5개의 점수가 (3,3,4,2,2) 라고 하면
   최고점수 4를 하나 제외하고, 최저점수 2를 하나 제외하고 (3,3,2)를 받게 됨.
   * 최종적으로 받은 3개의 점수와 교수자의 평가를 합하여 최종 점수 부여
   * 최종 점수를 기준으로 절대평가하여 성적 부여
- 저는 어떤 5명을 평가하게 되나요?
   * 어느 학생이 어떤 5명의 학생을 평가하는지는 추후 공지
-Doc-
그래프 1 파이 그래프 (각 산업별 비중)
그래프 2 꺾은선 그래프 (각 산업별 매출 추이)
그래프 3 꺾은선 그래프 (각 산업별 고용자 수 추이)
"""

from matplotlib.animation import FuncAnimation
# import seaborn as sns
import csv
# %%
import pandas as pd
import matplotlib.pyplot as plt

# 5 3 3
SalesOfICT = pd.read_csv('Sales_of_ICT_industry.csv')
ManpowerOfICT = pd.read_csv('Manpower_of_ICT.csv')
print("---------------------------------------")
print(ManpowerOfICT.iloc[0])
ManpowerOfICT.set_index('시점',inplace=True)
ManpowerOfICT.index.values[0] = '대분류'
ManpowerOfICT.index.values[1] = '소분류'
ManpowerOfICT.columns = [[
    '항목',
    '정보통신방송기기업', '정보통신방송기기업', '정보통신방송기기업',
    '정보통신방송기기업', '정보통신방송기기업', '정보통신방송기기업',
    '정보통신방송서비스업', '정보통신방송서비스업', '정보통신방송서비스업',
    '정보통신방송서비스업', '소프트웨어 개발 및 제작업', '소프트웨어 개발 및 제작업',
    '소프트웨어 개발 및 제작업', '소프트웨어 개발 및 제작업'
],ManpowerOfICT.iloc[0]]
print("---------------------------------------")
print(ManpowerOfICT.iloc[0])
print("---------------------------------------")
ManpowerOfICT.index.values[0] = '대분류'
ManpowerOfICT.index.values[1] = '소분류'
print(ManpowerOfICT.iloc[0])
print("---------------------------------------")
print(ManpowerOfICT.iloc[0, 2:7])
print(ManpowerOfICT.iloc[0, 6:9])
print(ManpowerOfICT.iloc[0, 9:12])
print(ManpowerOfICT.index)
ManpowerOfICT.index.values[0] = '대분류'
ManpowerOfICT.index.values[1] = '소분류'
print(ManpowerOfICT)
df1 = pd.DataFrame(ManpowerOfICT,
                   columns=[ManpowerOfICT.iloc[0],
                            ManpowerOfICT.iloc[1]])
df1.columns.names = ["Cidx1", "Cidx2"]
print(df1)
#
# df1 = ManpowerOfICT.iloc[[0, -1],0:]
# print(df1)
# print(df1.iloc[0,1])

# # info. of groups
# group_names = ['정보통신방송기기업', '정보통신방송서비스업', '소프트웨어 개발 및 제작업']
# group_sizes = [95, 54, 25]
# # info. of subgroups
# subgroup_names = ['A_1', 'A_2', 'A_3', 'A_4',
#                   'B_1', 'B_2', 'B_3',
#                   'C_1', 'C_2']
# subgroup_sizes = [50, 30, 10, 5, 30, 20, 4, 20, 5]
# # colors
# a, b, c = [plt.cm.Reds, plt.cm.Greens, plt.cm.Blues]
# # width
# width_num = 0.4
# # Outside Ring
# fig, ax = plt.subplots()
# ax.axis('equal')
# pie_outside, _ = ax.pie(group_sizes,
#                         radius=1.3,
#                         labels=group_names,
#                         labeldistance=0.8,
#                         colors=[a(0.6), b(0.6), c(0.6)])
# plt.setp(pie_outside,
#          width=width_num,
#          edgecolor='white')
# # Inside Ring
# pie_inside, plt_labels, junk = \
#
#     ax.pie(subgroup_sizes,
#            radius=(1.3 - width_num),
#            labels=subgroup_names,
#            labeldistance=0.75,
#            autopct='%1.1f%%',
#            colors=[a(0.5), a(0.4), a(0.3), a(0.2),
#                    b(0.5), b(0.4), b(0.3),
#                    c(0.5), c(0.4)])
# plt.setp(pie_inside,
#          width=width_num,
#          edgecolor='white')
# plt.title('Donut Plot with Subgroups', fontsize=20)
# plt.show()


# print(ManpowerOfICT.loc[['2019 p)']])
# ManpowerOfICT['시점'] = pd.to_datetime(ManpowerOfICT['시점'])

# plt.pie(ratio, labels=df1.iloc[0,1], shadow=True, startangle=270)
plt.show()
'''
nq['Date'] = pd.to_datetime(nq['Date'])
nq.set_index(nq['Date'], inplace=True)

print(ks.head())
print(nq.head())
'''

"""
그래프 1 파이 그래프 (각 산업별 비중, 2019)
그래프 2 꺾은선 그래프 (각 산업별 매출 추이, 2011.01~2019.11)
그래프 3 꺾은선 그래프 (각 산업별 고용자 수 추이, 2011~2019)
그래프 4 꺾은선 그래프 (각 산업별 인당 연평균 매출 추이, 2011~2019)
"""

# plt.rc('font', family='Malgun Gothic')
# fig = plt.figure(figsize=(6, 4))
# fig.autofmt_xdate(bottom=0.2, rotation=75, ha='right')
# plt.subplot(211)
# plt.title("KOSPI")
# plt.grid()
# plt.xlabel("Time")
# plt.ylabel("￦")
# plt.plot(ks['Date'], ks['Close'])
# plt.subplot(212)
# plt.title("NASDAQ")
# plt.grid()
# plt.xlabel("Time")
# plt.ylabel("$")
# plt.plot(nq['Date'], nq['Close'])
#
# # 수익률
# incomeRate(ks)
# ks_income_data = ks[['Adj Close', 'PriceLag1', 'PriceDiff', 'DailyReturn', 'UpDown']]
# print(ks_income_data)
# ks['UpDown'].value_counts()
# plt.figure(figsize=(6, 4))
# plt.plot(ks.index, ks['DailyReturn'], color='lightblue')
# plt.axhline(y=0, color='red', ls='--')
#
# incomeRate(nq)
# nq_income_data = ks[['Adj Close', 'PriceLag1', 'PriceDiff', 'DailyReturn', 'UpDown']]
# print(nq_income_data)
# ks['UpDown'].value_counts()
# plt.figure(figsize=(6, 4))
# plt.plot(nq.index, nq['DailyReturn'], color='lightblue')
# plt.axhline(y=0, color='red', ls='--')
#
# plt.show()
