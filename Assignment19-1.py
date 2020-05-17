# %% [과제 19-1] subset_iloc_range=df.iloc[[0,9,99],[0,3,5]]동일한 결과를 주는 코드를
# loc속성을 이용하여 작성하시오.
import pandas as pd

df = pd.read_csv('gapminder.tsv', sep='\t')
print(df.head())
# print("iloc : Purely integer-location based indexing for selection by position.")
subset_iloc_range = df.iloc[[0, 9, 99], [0, 3, 5]]
print(subset_iloc_range)

# print(".loc[] is primarily label based, but may also be used with a boolean array.")
subset_loc_range = df.loc[[0, 9, 99], ['country', 'lifeExp', 'gdpPercap']]
print(subset_loc_range)
subset_loc_range = df.loc[[0, 9, 99], ['country', 'lifeExp', 'gdpPercap']]
print(subset_loc_range)