#Tests_panda
import pandas as pd
import numpy as np
df = pd.read_csv('https://bit.ly/ds-korean-idol')
df2=df.copy()
df2_drop=df2.drop([1,3],axis=0)
print(df2_drop.head())