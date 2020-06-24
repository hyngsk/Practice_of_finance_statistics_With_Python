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

그래프 1 파이 그래프 (ICT산업별 인력현황 (2019))
그래프 2 꺾은선 그래프 (ICT산업별 매출현황 (2019))
그래프 3 꺾은선 그래프 (각 산업별 고용자 수 추이, 2011~2019)
그래프 4 꺾은선 그래프 (각 산업별 인당 연평균 매출 추이, 2011~2019)

"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 5 3 3
SalesOfICT = pd.read_csv('Sales_of_ICT_industry.csv')
ManpowerOfICT = pd.read_csv('Manpower_of_ICT.csv')

# %%
# ManpowerOfICT 데이터 가공
df = pd.DataFrame(ManpowerOfICT.values[1:10, 0:],
                  columns=[[
	                  '',
	                  '항목',
	                  '정보통신방송기기업', '정보통신방송기기업', '정보통신방송기기업',
	                  '정보통신방송기기업', '정보통신방송기기업', '정보통신방송기기업',
	                  '정보통신방송서비스업', '정보통신방송서비스업', '정보통신방송서비스업',
	                  '정보통신방송서비스업', '소프트웨어 개발 및 제작업', '소프트웨어 개발 및 제작업',
	                  '소프트웨어 개발 및 제작업', '소프트웨어 개발 및 제작업'
                  ], ManpowerOfICT.iloc[0]])
df.set_index('', inplace=True)
df.columns.names = ['대분류', '소분류']
df.index.names = ['시점']

# SalesOfICT 데이터 가공
df1 = pd.DataFrame(SalesOfICT.values[1:, 0:],
                   columns=[[
	                   '',
	                   '정보통신방송기기업', '정보통신방송기기업', '정보통신방송기기업',
	                   '정보통신방송기기업', '정보통신방송기기업', '정보통신방송서비스업',
	                   '정보통신방송서비스업', '정보통신방송서비스업', '소프트웨어 개발 및 제작업',
	                   '소프트웨어 개발 및 제작업', '소프트웨어 개발 및 제작업'
                   ], SalesOfICT.iloc[0]])
df1.set_index('', inplace=True)
df1.columns.names = ['대분류', '소분류']
df1.index.names = ['시점']
# 가공한 데이터의 타입 변경
df = df.apply(pd.to_numeric, errors='coerce').fillna(0)
df1 = df1.apply(pd.to_numeric, errors='coerce').fillna(0)

# %%
# 그래프 1 파이 그래프 (각 산업별 비중, 2019)
# info. of groups
group_names = [df.columns[2][0], df.columns[8][0], df.columns[12][0]]
group_sizes = [df.loc['2019 p)', (group_names[0], '소계')],
               df.loc['2019 p)', (group_names[1], '소계')],
               df.loc['2019 p)', (group_names[2], '소계')]]

subgroup_names = [df.columns[2][1], df.columns[3][1], df.columns[4][1],
                  df.columns[5][1], df.columns[6][1], df.columns[8][1],
                  df.columns[9][1], df.columns[10][1], df.columns[12][1],
                  df.columns[13][1], df.columns[14][1]]

subgroup_sizes = [df.loc['2019 p)', (group_names[0], subgroup_names[0])],
                  df.loc['2019 p)', (group_names[0], subgroup_names[1])],
                  df.loc['2019 p)', (group_names[0], subgroup_names[2])],
                  df.loc['2019 p)', (group_names[0], subgroup_names[3])],
                  df.loc['2019 p)', (group_names[0], subgroup_names[4])],
                  df.loc['2019 p)', (group_names[1], subgroup_names[5])],
                  df.loc['2019 p)', (group_names[1], subgroup_names[6])],
                  df.loc['2019 p)', (group_names[1], subgroup_names[7])],
                  df.loc['2019 p)', (group_names[2], subgroup_names[8])],
                  df.loc['2019 p)', (group_names[2], subgroup_names[9])],
                  df.loc['2019 p)', (group_names[2], subgroup_names[10])]]

# %%
# 파이차트의 내부차트 레이블 만드는 함수 (출처 : matplotlib.org 사이트)
plt.rc('font', family='Malgun Gothic')
a, b, c = [plt.cm.Reds, plt.cm.Greens, plt.cm.Blues]
width_num = 0.4
# Outside Ring
fig, ax = plt.subplots(figsize=(15, 20), subplot_kw=dict(aspect="equal"))
plt.rc('font', family='Malgun Gothic')
pie_outside, _ = ax.pie(group_sizes, radius=1, labels=group_names,
                        colors=[a(0.6), b(0.6), c(0.6)],
                        startangle=270,
                        wedgeprops=dict(width=0.3, edgecolor='w'),
                        shadow=True)
plt.setp(pie_outside, width=width_num, edgecolor='white')
# Inside Ring
plt.rc('font', family='Malgun Gothic')
pie_inside, plt_labels, junk = ax.pie(subgroup_sizes, radius=(1 - width_num),
                                      labeldistance=1, autopct='%1.1f%%', pctdistance=1.2,
                                      colors=[a(0.2), a(0.3), a(0.4), a(0.5), a(0.6),
                                              b(0.2), b(0.3), b(0.4),
                                              c(0.2), c(0.3), c(0.4)],
                                      startangle=270)
plt.setp(pie_inside, width=width_num, edgecolor='white')

bbox_props = dict(boxstyle="square,pad=0.4", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")
for i, p in enumerate(pie_inside):
	plt.rc('font', family='Malgun Gothic')
	ang = (p.theta2 - p.theta1) / 2. + p.theta1
	y = np.sin(np.deg2rad(ang))
	x = np.cos(np.deg2rad(ang))
	horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
	connectionstyle = "angle,angleA=0,angleB={}".format(ang)
	kw["arrowprops"].update({"connectionstyle": connectionstyle})
	ax.annotate(subgroup_names[i], xy=(x, y), xytext=(1 * np.sign(x), 1.2 * y),
	            horizontalalignment=horizontalalignment, **kw)

plt.title('ICT산업별 인력현황 (2019)', loc='center', pad=10, fontsize=16)
plt.show()

# %%
a, b, c = [plt.cm.Reds, plt.cm.Greens, plt.cm.Blues]
width_num = 0.4
# Outside Ring
fig2, ax = plt.subplots(figsize=(15, 20), subplot_kw=dict(aspect="equal"))
wedges, texts = ax.pie(subgroup_sizes, radius=1, wedgeprops=dict(width=0.5), startangle=270)

bbox_props = dict(boxstyle="square,pad=0.4", fc="w", ec="k", lw=0.72)
kw2 = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")
for i, p in enumerate(wedges):
	ang = (p.theta2 - p.theta1) / 2. + p.theta1
	y = np.sin(np.deg2rad(ang))
	x = np.cos(np.deg2rad(ang))
	horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
	connectionstyle = "angle,angleA=0,angleB={}".format(ang)
	kw2["arrowprops"].update({"connectionstyle": connectionstyle})
	ax.annotate(subgroup_names[i], xy=(x, y), xytext=(1 * np.sign(x), 1.2 * y),
	            horizontalalignment=horizontalalignment, **kw2)
plt.rc('font', family='Malgun Gothic')
plt.title('ICT산업별 매출현황 (2019)', loc='center', pad=10, fontsize=16)
plt.show()
# %%
# 그래프 2 꺾은선 그래프 (각 산업별 매출 추이, 2011.01~2019.11)
# 그래프 3 꺾은선 그래프 (각 산업별 고용자 수 추이, 2011~2019)

df.plot(title='연도별 ICT산업 종사자 추이', figsize=[15, 8], label='일교차')
# colors = plt.cm.jet(np.linspace(0,1,))
df1.plot(df1.index, df1['소계'], title = '연도별 ICT산업 매출액 추이', figsize = [15, 8])
# x=df.index
# y=group_names
# plt.plot(x,y, figsize=[20, 20])
# sns.jointplot(x='전자부품업', y='컴퓨터 및 주변기기엄', data=df, hue='시점')
# ax = df1.plot(kind='barh', stacked=True, title="년도별 연령대 이용비율(%)", rot=0)
# for p in ax.patches:
#    left, bottom, width, height = p.get_bbox().bounds 
#    ax.annotate("%.1f"%(width*100), xy=(left+width/2, bottom+height/2), ha='center', va='center')
# plt.box(False)
# plt.show()

# %%
# 그래프 4 꺾은선 그래프 (각 산업별 인당 연평균 매출 추이, 2011~2019)
x = df.index
y = subgroup_names
# df.plot(df.index, subgroup_names, figsize=[20, 20])
ax = df.plot(legend=False)
for p in ax.patches:
	left, bottom, width, height = p.get_bbox().bounds
	ax.annotate("%.1f" % (height * 100), xy=(left + width / 2, bottom + height / 2), ha='center', va='center')
plt.sca(ax)

plt.box(False)
