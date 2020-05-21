# [과제 31-1] 위의 코드에서 평균을 제대로 구할 수 있도록 수정해서 제출하세요.
# Hint: 자료의 개수를 세고 저장할 변수를 만들어 sum에 나누어 주세요.

import pandas as pd


def avg(col):
    sum, count = 0, 0
    for item in col:
        sum += item
        count += 1
    return sum / count


df = pd.DataFrame(
    {'a': [10, 20, 30], 'b': [20, 30, 40], 'c': [30, 40, 50]})
print(df.apply(avg))

df2 = pd.DataFrame(
    {'a': [10, 20, 30, 40], 'b': [20, 30, 40, 50], 'c': [30, 40, 50, 60], 'd': [40, 50, 60, 70]})
print(df2.apply(avg))

