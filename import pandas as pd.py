import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
mpl.rcParams['font.family']='Apple SD Gothic Neo'
plt.rcParams["figure.figsize"] = (12, 9)

plt.plot(np.arange(10), np.arange(10)*2)
plt.plot(np.arange(10), np.arange(10)**2)
plt.plot(np.arange(10), np.log(np.arange(10)))

# 타이틀 & font 설정
plt.title('범례 설정 예제입니다', fontsize=20)

# X축 & Y축 Label 설정
plt.xlabel('X축', fontsize=20)
plt.ylabel('Y축', fontsize=20)

# X tick, Y tick 설정
plt.xticks(rotation=90)
plt.yticks(rotation=30)

# legend 설정
plt.legend(['10 * 2', '10 ** 2', 'log'], fontsize=15)

plt.show()