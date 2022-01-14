import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

x = np.random.rand(50)
y = np.random.rand(50)
area = x * y * 1000

sns.scatterplot(x, y, size=area, sizes=(area.min(), area.max()), hue=area, palette='gist_gray')
plt.show()

