# [과제 41-1] "gapminder.tsv" 데이터에 대하여 FacetGrid를 사용하여 국가별 lifeExp, pop,gdpPercap
# 의 데이터를 설명할 그래프를 그려보시오.
# 예제:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('gapminder.tsv', sep='\t')
#
#%%
# 년도에 따른 모든 국가의 기대수명(lifeExp)에대한 1인 총 생산(gdpPercap)
facet = sns.FacetGrid(df, height=3, col_wrap=2, col='year', hue='country')
facet.map(plt.scatter, 'lifeExp', 'gdpPercap')
facet.add_legend()
plt.show()

#%%
# 년도에 따른 나라별 인구 변화
facet = sns.FacetGrid(df, height=3, col_wrap=4, col='country', hue='country')
facet.map(plt.plot,'year','pop')
facet.add_legend()
plt.show()
#%%
# # 년도에 따른 나라별 1인 총 생산(gdpPercap)
facet = sns.FacetGrid(df, height=3, col_wrap=4,col='country', hue='country')
facet.map(plt.plot,'year','gdpPercap')
facet.add_legend()
plt.show()
#%%
# 각 국가의 년도별 기대수명(lifeExp)에대한 1인 총 생산(gdpPercap)
facet = sns.FacetGrid(df, height=3,col_wrap=4,col='country', hue='year')
facet.map(plt.scatter,'lifeExp','gdpPercap')
facet.add_legend()
plt.show()