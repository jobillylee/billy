#Tests_panda
import pandas as pd
import numpy as np
df = pd.read_csv('https://bit.ly/ds-korean-idol')
df2 = pd.read_csv('https://bit.ly/ds-korean-idol-2')
df2_drop=df2.drop([1,3,5],axis=0)
df_merge=pd.merge(df, df2_drop, on='이름', how='outer')
print(df_merge.head())