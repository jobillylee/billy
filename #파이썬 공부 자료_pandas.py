#파이썬 공부 자료_pandas

import pandas as pd
<pandas>
    <01.Series,Dataframe>
        #가.series
        #series는 1차원의 값, 엑셀 데이터에서 보면 한개 열/컬럼의 값
        pd.Series([1,2,3,4])
        0    1
        1    2
        2    3
        3    4
        dtype: int64
        #변수 활용해 Series를 만들 수 있다
        data=[1,2,3,4]
        pd.Series(data)
        0    1
        1    2
        2    3
        3    4
        dtype: int64

        #나.dataframe
        #데이터프레임은 2차원 이상의 값, 엑셀과 유사
        #데이터프레임을 만드는 방법은 두가지
        company1 = [['삼성', 2000, '스마트폰'],['현대', 1000, '자동차'],['네이버', 500, '포털']]
        excel=pd.DataFrame(company1) #company1 데이터 프레임을 만들고
        excel.columns=['기업','매출액','주력상품'] #제목 컬럼을 생성
        기업   매출액  주력상품
        0   삼성  2000  스마트폰
        1   현대  1000   자동차
        2  네이버   500    포털