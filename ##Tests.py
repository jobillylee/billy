#Tests_panda
import pandas as pd
import numpy as np
df = pd.read_csv('https://bit.ly/ds-korean-idol')
df2 = pd.read_csv('https://bit.ly/ds-korean-idol-2')
my_map={'남자':1, '여자':0}
df['성별']=df['성별'].map(my_map)
print(df.head())