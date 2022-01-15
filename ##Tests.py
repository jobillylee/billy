#Tests_panda

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

titanic = sns.load_dataset('titanic')
tips = sns.load_dataset('tips')

#폰트셋팅
sns.lmplot(x='total_bill',y='tip',hue='smoker',col='day',col_wrap=2,height=8,data=tips)

plt.show()