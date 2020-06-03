# coding=utf-8
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")


def recode_sex(sex):
    if sex == 'Female':
        return 0
    else:
        return 1


tips['sex_color'] = tips['sex'].apply(recode_sex)

scatter_plot = plt.figure ()
axes1 = scatter_plot.add_subplot(1, 1, 1)
axes1.scatter (x=tips['total_bill'],
               y=tips['tip'],
               s=tips['size'] * 10,  # size (점의 크기)
               c=tips['sex_color'],  # color (점의 색깔)
               alpha=0.5)  # alpha는 점의 투명도
axes1.set_title('Total Bill vs Tip Colored by Sex and Size')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')
