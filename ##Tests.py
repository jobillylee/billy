#Tests_pandas
import pandas as pd
company1 = [['삼성', 2000, '스마트폰'],['현대', 1000, '자동차'],['네이버', 500, '포털']]
excel=pd.DataFrame(company1)
excel.columns=['기업','매출액','주력상품']
print(excel)