#Tests_panda
import pandas as pd
df=pd.read_csv('http://bit.ly/ds-korean-idol')
new_columns=['name','group','소속사', '성별', '생년월일', '키', '혈액형', '브랜드평판지수']
df.columns=new_columns
print(df.sort_index())