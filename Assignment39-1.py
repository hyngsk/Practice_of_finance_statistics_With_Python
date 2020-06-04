# [과제 39-1] 위의 tip에 대한 산점도에서 범례 등을 추가하여 그래프를 화려하게
# 꾸며보세요.

import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')


def recode_sex(sex):
	if sex == 'Female':
		return 0
	else:
		return 1


tips['sex_color'] = tips['sex'].apply(recode_sex)

female = tips.loc[tips['sex_color'] == 0, :]
male = tips.loc[tips['sex_color'] == 1, :]
scatter_plot = plt.figure(dpi=150)

axes1 = scatter_plot.add_subplot(1, 1, 1)
axes1.scatter(x=female['total_bill'],
			y=female['tip'],
			s=female['size'] * 10,
			c='lawngreen',
			marker='8',
			label='female',
			alpha=0.5)
axes1.scatter(x=male['total_bill'],
			y=male['tip'],
			s=male['size'] * 10,
			color='blueviolet',
			marker='*',
			label='male',
			alpha=0.5)

axes1.set_title('Total Bill vs Tip Colored by Sex and Size')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')
plt.legend(loc='upper left', fontsize='xx-small')
plt.show()
