#Tests_panda
import pandas as pd
df=pd.read_csv('http://bit.ly/ds-korean-idol')  
df.loc[df['이름']=='지드래곤','국적']='korea'
print(df.head())
