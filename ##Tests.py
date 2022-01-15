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
sns.jointplot(x='total_bill',y='tip',hue='sex',kind='rug',height=8,palette='muted',data=tips)

plt.show()