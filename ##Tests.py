#Tests_panda

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
#폰트셋팅
mpl.rcParams['font.family']='Apple SD Gothic Neo'
plt.rcParams["figure.figsize"] = (12, 12)
#데이터 1
data1=np.arange(1, 50)
data2=np.arange(3, 50)
data3=np.arange(10,50)
        
fig, axes = plt.subplots(3,2)
        
axes[0,0].plot(data1)
axes[1,0].plot(data2)
axes[2,0].plot(data3)
axes[0,1].plot(data1)
axes[1,1].plot(data2)
axes[2,1].plot(data3)

plt.savefig("사본1",bpi=3.3)
        
plt.show()