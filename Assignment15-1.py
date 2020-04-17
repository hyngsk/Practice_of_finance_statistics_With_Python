# %% [과제15-1] 지난 시간 학습했던 다음 코드를 numpy를 사용하여 변경하여 코드와
# 결과물을 제출하세요.
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(50, 100, 100)
y = np.random.randint(50, 100, 100)
size = np.random.randint(10, 100, 100)

plt.scatter(x, y, s=size, c=size, cmap='spring')
plt.colorbar()
plt.show()
