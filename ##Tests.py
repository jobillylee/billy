#Tests_panda

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

#폰트셋팅
mpl.rcParams['font.family']='Apple SD Gothic Neo'
plt.figure(figsize=(12,6))

titanic = sns.load_dataset('titanic')
x=titanic.corr()
sns.heatmap(x,annot=True,cmap='YlGnBu')

plt.show()



