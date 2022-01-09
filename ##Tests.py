#Tests_panda
import pandas as pd
df=pd.read_csv('http://bit.ly/ds-korean-idol')
my_needs=['SM','빅히트']
print(df.loc[df['소속사'].isin(my_needs),'이름'])