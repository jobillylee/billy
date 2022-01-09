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
        #리스트로 dataframe 만들기
        company1 = [['삼성', 2000, '스마트폰'],['현대', 1000, '자동차'],['네이버', 500, '포털']]
        excel=pd.DataFrame(company1) #company1 데이터 프레임을 만들고
        excel.columns=['기업','매출액','주력상품'] #제목 컬럼을 생성
        print(excel)
        기업   매출액  주력상품
        0   삼성  2000  스마트폰
        1   현대  1000   자동차
        2  네이버   500    포털
        #dict로 dataframe 만들기
        company2 = {'기업명':['삼성', '현대', '네이버'], 
                    '매출액': [2000, 1000, 500], 
                    '업종': ['스마트폰', '자동차', '포털']}
        excel2=pd.DataFrame(company2)
        print(excel2)
        기업명   매출액  주력상품
        0   삼성  2000  스마트폰
        1   현대  1000   자동차
        2  네이버   500    포털

        #다. index 
        excel2['기업명']
        기업  
        0   삼성 
        1   현대 
        2  네이버  
        #index를 특정 컬럼으로 지정하기 
        excel2.index=excel2['매출액']
              기업명   매출액    업종
        매출액                  
        2000   삼성  2000  스마트폰
        1000   현대  1000   자동차
        500   네이버   500    포털

    <2.파일 불러오기>
        #파일을 불러올 때 다양한 함수를 사용 원하는 파일을 불러올 수 있다
        #가.pd.read_csv(#경로/파일명 or #URL)
        ad=pd.read_csv('/Users/leejuho/Documents/gitTest/korean-idol.csv')
        
        #나.csv 구분자가 ',' 가 아닌 다른 기호 일 때 불러오면 오류가 생긴다 
        #이럴 경우 sep으로 구분자를 지정해줘야 한다, 탭 구분은 '\t'
        ad=pd.read_csv('/korean-idol.csv', sep='|')

        #다.csv 불러 올 때 첫번째 열을 지정할 수 있다. index_cel=0(위치), index_cel='컬럼'
        ad=pd.read_csv('/korean-idol.csv', sep='|', index_col='기업명')

        #라.컬럼명이 없는 경우 지정할 수 있다 name=['ID','A','B','C'],header=none
        ad=pd.read_csv('/korean-idol.csv', sep='|', name=['ID','A','B','C'],header=None)
        #header=None은 컬럼명이 없단는 의미, header=0은 첫번째 열 값이 컬럼이라는 의미

        #마.한글을 인코딩 할 때 파이썬과 csv가 안맞으면 오류가 발생한다. 이럴 경우 인코딩 값을 지정해 줘야 한다
        ad=pd.read_csv('/korean-idol.csv',encoding='utf-8')
        #일반적으로 utf-8, 윈도우에서 자주 쓰이는 건 CP949, 안되면 latin

        #바. 특정 열을 빼고 데이터 값을 가져올 수 있다 skiprows=
        ad=pd.read_csv('/korean-idol.csv',skiprows=[1,2])
        #이렇게 지정하면 1,2행을 빼고 3번쨰 향부터 추출한다

        #사. 상위 n번째 행까지 추출할 수 있다. nrows=n
        ad=pd.read_csv('/korean-idol.csv',nrows=3)

        #아. 결측값(missing value)을 지정해 해당 값이 문자가 아닌 결측값이라 지정해 줘야 분석이 틀리지 않을 수 있다
        ad=pd.read_csv('/korean-idol.csv',na_values=['??','N/A']

        #다.컬럼(열) 단위 데이터 유형을 지정할 수 있다.
        ad=pd.read_csv('/korean-idol.csv',dtype = {"ID": int, "LAST_NAME": str, "AGE": float})

    <3.통계값(describe),요약정보(info),정렬(sort)>
        df=pd.read_csv('http://bit.ly/ds-korean-idol')
        #가.컬럼(열) 명칭 변경
        print(df.columns)
        #index(['이름', '그룹', '소속사', '성별', '생년월일', '키', '혈액형', '브랜드평판지수'], dtype='object')
        new_columns=['name','group','소속사', '성별', '생년월일', '키', '혈액형', '브랜드평판지수']
        df.columns=new_columns
        print(df.columns)
        #Index(['name', 'group', '소속사', '성별', '생년월일', '키', '혈액형', '브랜드평판지수'], dtype='object')

        #나.행 정보 출력 index
        print(df.index)
        #RangeIndex(start=0, stop=15, step=1)

        #다.기존적인 행의 정보 출력 info()
        print(df.info())
        RangeIndex: 15 entries, 0 to 14
        Data columns (total 8 columns):
         #   Column   Non-Null Count  Dtype  
        ---  ------   --------------  -----  
         0   name     15 non-null     object 
         1   group    14 non-null     object 
         2   소속사      15 non-null     object 
         3   성별       15 non-null     object 
         4   생년월일     15 non-null     object 
         5   키        13 non-null     float64
         6   혈액형      15 non-null     object 
         7   브랜드평판지수  15 non-null     int64  
        dtypes: float64(1), int64(1), object(6)
        memory usage: 1.1+ KB
        None
        #count 갯수는 빠진 값을 찾아내는 용도
        #Dtype은 해당 컬럼 값을 타입을 확인, object는 dict

        #라.통계 정보 확인 describe, 산술 계산이 가능한 int, float 값만 출력
        print(df.describe())
           키       브랜드평판지수
        count   13.000000  1.500000e+01 #row행의 갯수
        mean   175.792308  5.655856e+06 #평균
        std      5.820576  2.539068e+06 #표준 편차
        min    162.100000  2.925442e+06 #최소값
        25%    174.000000  3.712344e+06 #상위 25%
        50%    177.000000  4.668615e+06
        75%    179.200000  7.862    214e+06
        max    183.000000  1.052326e+07 #전체
        #describe은 산술 계산을 할 수 있는 컬럼만 출력

        #마.데이터 형태 shape
        print(df.shape)
        (15, 8)

        #바.index 위치 기준 상하위 값 출력
        head() #상위 5개
        tail() 하위 5개
        head(3) #상위 3개

        #사. 정렬(sort)
        #sort는 기본적으로 오름차순 정렬, sort에는 index , value 2가지가 있다
        print(df.sort_index()) #내림차순 정렬 시 ascending=False로 입역
        print(df.sort_value(by='키')) #특정 컬럼 기준으로 정렬
        print(df.sort_value(by='키', ascending=False)) # 내림차순 정열
        df.sort_values(by=['키', '브랜드평판지수']) #두가지 이상 컬럼 기준 정렬 시

    <Selection>
        #가.컬럼 선택
        #df[''],df[""],df.컬럼
        import pandas as pd
        df=pd.read_csv('http://bit.ly/ds-korean-idol')
        df['키']
        df["키"]
        df.키

        #나. 행과 열의 구간(범위) 선택하기
        #loc 함수는 칼럼과 인덱스를 직접 선택하여 selection 하는 방식으로 
        #구간을 구할 때 numpy의 index 방식을 따르지 않는다
        #기준 값이 숫자일 때
        df.loc[3:8,['이름','성별']] #[행,컬럼]
           이름  성별
        3   뷔  남자
        4  화사  여자
        5  정국  남자
        6  민현  남자
        7  소연  여자
        8   진  남자

        #인덱스의 값(행 기준 값)이 문자일 때
        #행과 열 모두 구간별 및 이름별로 selection 할 수 있으며, 반드시
        #출력 값의 순서대로 입력하여 추출해야 한다
        df.index=df['이름']
        df1=df.loc['화사':'진',['그룹','소속사']]
        print(df1)
            그룹   소속사
        이름             
        화사    마마무   RBW
        정국  방탄소년단   빅히트
        민현   뉴이스트  플레디스
        소연    아이들    큐브
        진   방탄소년단   빅히트

        #컬럼 영역을 구간으로 구하고 싶을 경우 []을 빼고 작성한다
        df.index=df['이름']
        df1=df.loc['화사':'진','그룹':'소속사']
        print(df1)  
            그룹   소속사
        이름             
        화사    마마무   RBW
        정국  방탄소년단   빅히트
        민현   뉴이스트  플레디스
        소연    아이들    큐브
        진   방탄소년단   빅히트      

        #다.행과 열 구간(범위) 선택하기
        #iloc은 numpy index 형식으로 dataframe 중 데이터를 추출할 때 쓴다
        print(df.iloc[1:3,0:3])
             이름   그룹  소속사
        1  지드래곤   빅뱅   YG
        2  강다니엘  NaN  커넥트

        #조건을 활용한 색인 (Boolean indexing)
        print(df['키']>180) #df dataframe에서 키가 180보다 큰 사람을 True, 작으면 False로 
        0     False
        1     False
        2     False
        3     False
        4     False
        5     False
        6      True
        7     False
        8     False
        9     False
        10    False
        11     True
        12    False
        13    False
        14    False
        Name: 키, dtype: bool
        #dataframe에서 조건에 맞는 데이터를 컬럼 지정하여 추출
        print(df[df['키']>180]['이름']) #조건에 맞는 사람의 데이터를 추출하되, 이름 컬럼만 추출
        6      민현
        11    차은우
        print(df.loc[df['키']>180,'이름']) #위 로직과 동일 loc함수 사용

        #라.원하는 데이터가 list로 있을 때 색인 하는 방법
        my_needs=['SM','빅히트']
        print(df.isin(my_needs)) #전체 데이터 프레임에서 list 색인
               이름     그룹    소속사     성별   생년월일      키    혈액형  브랜드평판지수
        0   False  False   True  False  False  False  False    False
        1   False  False  False  False  False  False  False    False
        2   False  False  False  False  False  False  False    False
        3   False  False   True  False  False  False  False    False
        4   False  False  False  False  False  False  False    False
        5   False  False   True  False  False  False  False    False
        6   False  False  False  False  False  False  False    False
        7   False  False  False  False  False  False  False    False
        8   False  False   True  False  False  False  False    False
        9   False  False  False  False  False  False  False    False
        10  False  False   True  False  False  False  False    False
        11  False  False  False  False  False  False  False    False
        12  False  False  False  False  False  False  False    False
        13  False  False  False  False  False  False  False    False
        14  False  False   True  False  False  False  False    False
        
        print(df['소속사'].isin(my_needs)) #소속사 컬럼 데이터에서 my_needs list 색인
        0      True
        1     False
        2     False
        3      True
        4     False
        5      True
        6     False
        7     False
        8      True
        9     False
        10     True
        11    False
        12    False
        13    False
        14     True
        Name: 소속사, dtype: bool
        
        #list 조건에 맞는 값을 색인한 값을 추출하는데, 이름 컬럼만
        print(df.loc[df['소속사'].isin(my_needs),'이름']) 
        0     지민
        3      뷔
        5     정국
        8      진
        10    태연
        14    슈가
        Name: 이름, dtype: object
        










