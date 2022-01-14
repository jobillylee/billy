#Tests_panda

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

#폰트셋팅
mpl.rcParams['font.family']='Apple SD Gothic Neo'

#데이터 1
x = np.random.rand(50)
y = np.random.rand(50)
area = x * y * 1000

plt.figure(figsize=(12,6))

plt.subplot(131)
plt.title('alpha=0.9')
plt.ylabel('Y축')
sns.scatterplot(x,y,size=area,sizes=(area.min(),area.max()),hue=area,palette='gist_gray',alpha=0.9,sharey=True)

plt.subplot(132)
plt.title('alpha=0.6')
sns.scatterplot(x,y,size=area,sizes=(area.min(),area.max()),hue=area,palette='gist_gray',alpha=0.6)

plt.subplot(133)
plt.title('alpha=0.4')
sns.scatterplot(x,y,size=area,sizes=(area.min(),area.max()),hue=area,palette='gist_gray',alpha=0.4)

plt.show()