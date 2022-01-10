#Tests_panda
import pandas as pd
import numpy as np
df=pd.read_csv('http://bit.ly/ds-korean-idol')  
df_gv=df.groupby(['소속사','이름'])['키'].sum()
df_gv2=df_gv.unstack('소속사')
df_reset=df_gv2.reset_index()
print(df_reset)