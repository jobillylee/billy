#파이썬 공부 자료_기본편(21.12.27)

<기본편>
    <01.데이터 타입>
        #가.변수
        #알파벳 대소문 가능, 순서는 영어+숫자 / 숫자+영어 불가, 공백 불가, _제외 특수문자 불가
        가능:a=1 , a1=1 , a_=1 , 
        불가:!=1 / 1a=1 / a a=1
        
        #나.데이터 타입
        #int=정수 / float=실수 / str=문자 / bool=참 거짓 / none=Null 값을 넣는
        
        #다.데이터 타입(집합)
        #list
        #순서O, []표현, 시작부터 데이터 값을 지정 가능
        mylist=[1,2,3,4,5]
        mylist.append(1) #list 데이터 추가
        mylist.remove(1) #list 데이터 제거
        
        #tuple
        #순서O, 읽기 전용, ()표현, 시작부터 데이터 값을 지정 가능
        mytuple=(1,2,3,4,5)
        mytuple.append(1) #하면 에러 뜸, 읽기 전용이라 불가
        mytuple.remove(1) #불가
        mytuple[2]=5 #불가, 색인값 변경은 데이터 집합 상관 없이 []로 표현

        #set
        #순서X, 중복X, 변수에 set() 지정 필요
        myset=set() #set는 list, tuple과 다르게 데이터 집합을 바로 지정 가능 한지는 모르겠음
        type(myset)
        set
        #데이터 값을 추가해도 중복 불가라 집합에 추가되지 않음, {}로 출력값 표현됨 
        myset.add(1)
        myset.add(2)
        myset.add(2)
        myset
        {1,2}

        #dict
        #텍스트가 포함된 사전형 집행, key와 value쌍, 변수에 dict() 지정 필요, {}으로 표현됨
        mydict=dict()
        mydict[123]='abc'
        mydict['com']='def'
        mydict
        {123:'abc', 'com':'def'}
        len(mydict)
        2

        #라.색인(index)
        #집합 내 색인 시 왼쪽부터 0,1,2 순서대로 진행
        순서=[0,1,2,3,4,5]
        a=[1,2,3,4,5,6] #일 때 4를 찾는다면 
        a[3] #으로 데이터 색인
        
        #반대로 색인 시 오른쪽부터 순서대로 마이너스
        순서=[-5,-4,-3,-2,-1]
        a=[1,2,3,4,5,6] #일 때 4를 찾는다면 
        a[-3] #으로 데이터 색인

        #index로 접근 데이터 값 바꿀 때
        a=[1,2,3,4,5]
        a[2]=100
        a
        [1,2,100,4,5]

        #데이터 집합의 길이를 알고 싶으면 
        a=[1,2,3,4,5]
        len(a)
        5

    <2.연산>
        #기본적인 사칙연산은 엑셀과 동일, 파이썬에만 있는 특수 사칙연산 존재
        
        #%: 몫을 나눈 나머지 값
        a=10
        b=3
        a%b
        1

        #//: 나눗셈의 몫은 정수로 결과 출력
        a=10
        b=3
        a/b
        3.33333333333333
        a//b
        3

        #**: 제곱 연산
        10**2
        =100

        #문자열의 덧셈도 가능하다. -, /, *는 안된다
        a='사람'
        b='살려요'
        a+b
        '사람살려요'

    <03.함수>
        #가.indent(들여쓰기)
        #파이썬에서 들여쓰기는 단순 정리 개념이 아닌 하나의 언어
        # Tap키로 들여쓰기를 할 수 있다
        # : 다음에는 들어쓰기가 된다
        def my_func():
            print('')

        #나. 함수의 정의
        #함수는 입력값인 input과 결과값인 output(return) 존재
        #정해진 규칙에 따라 input과 return을 효율적으로 할 수 있도록 해주는 역할
        def myfunc(a,b,c):
            return (a+b)*c
        myfunc(1,2,3)
        9
        
        #다. 어법
        #어법은 def 함수이름 (피라미더1,피라미터2...)
        #리턴 값이 함수로 표현되는 경우는 리턴 지정을 안한다
        def my(a,b,c):
            print(a,b)
        my(1,3,4)
        
        #리턴 값이 수식인 경우는 리턴 삽입
        def myfunc(a,b,c,):
            s=a+b+c
            return s
        myfunc(1,2,3)
        6

        #리턴이 있는 경우 리턴 값을 변수로 할당, 결과 값을 다시 할당 할 수 있다
        result=myfunc(1,2,3)
        print(result+1)
        7

    <04.비교연산자>
        #대소 비교
        #>, >=, <=, <
        1>2
        False
        9<10
        True

        #같다, 같지 않다
        같다 ==, 같지 않다 !=

    <05.조건문>
        #가.if
        #if는 어떤 조건이 성립한다면, if 끝에는 반드시 : 삽입
        if 5<6:
            print('참')
        '참'
        if 5<3:
            print('참')
        print('끝')
        '끝'

        #나.else, elif
        #else는 if 구문 후 사용, if가 아닌 경우로 쓰임
        if 3<2:
            print('참')
        else:
            print('거짓')
        '거짓'
        #elif는 else가 중복 될 때 사용
        if 1>5:
            print('1이 참')
        elif 2>5:
            print('2가 참')
        elif 3>5:
            print('3이 참')
        elif 4>5:
            print('4가 참')
        else:
            print('5가 참')
        
        '5가 참'
        
        #다. 1=참,0=거짓
        if 1/0:
            print('참')
        else:
            print('거짓')
        '참'/'거짓'

    <6.논리연산자>
        #and
        #모든 조건이 만족할 때 참으로 인식
        true and true and false
        False
        true and true and True
        True

        #or
        #하나라도 조건이 만족하면 참으로 인식
        true or false or False
        True

    <07.반복문>
        #가.for
        #list, dict, set 등 집합을 순회돌며 반복할 때 사용
        # for 변수 in 집합 = for 하나씩 꺼내올 변수 in [집합]
        myfunc=[1,2,3,4]
        for abc in myfunc:
            print(abc)
        1
        2
        3
        4

        #짝수만 출력
        myfunc=[1,2,3,4]
        for abc in myfunc:
            if abc%2==1:
                continue
        print(abc)
        2
        4
        #continue는 조건이 만족할 시, 아래 구문을 실행하지 않고 상단으로 돌아가 다음 숫자를 반복하라
        #break는 조건이 만족되면 계산을 종료하라
        myfunc=[1,2,3,4]
        for abc in myfunc:
            if abc>=4:
                break
        print('abc')
        1
        2
        3

        #list comprehension
        my_func=[1,2,3,4,5]
        even=[i+1 for i in my_func if i%2==0]
        #for 문을 반복해서 수행하는데, if 구문에 적합할 시 i 리턴값에 +1한 값을 even에 저장한다
        even
        [3,5,7,9,11]

    <08.문자열 가지고 놀기>
        #가. 문자의 길이
        #문자는 공백까지 포함하여 길이가 계산된다
        a='나는 나다'
        len(a)
        5

        #나.문자 쪼개기(split)
        #split을 사용해 원하는 기준에 맞춰 문자를 나눠 list로 저장한다
        # 변수 지정 없는 split는 함수 적용 후 바로 이전 상태로 회귀, 변형된 상태가 계속되기 원하면 변수 지정 필수
        a='나는 나일까? 너일까?'
        a.split()
        ['나는','나일까?', '너일까?']
        a.split('?')
        ['나는 나일까', ' 너일까', '']
        a[0]
        '나는 나일까'

        #다.대소문자 (lower / upper)
        a='my Little babY'
        a.lower()
        'my little baby'
        a.upper()
        'MY LITTLE BABY'

        #라.~로 시작하는(startswith), ~로 끝나는(endswith)
        a='123.ppt'
        b='456.excel'
        c='789.word'
        ##
        a.startswith('4')
        False
        ##
        work=[a,b,c]
        study=[i for i in work if i.startswith('123')]
        study
        ['123.ppt']
        ##
        ##
        non_study=[b for b in work if b.endswith('word')]
        non_study
        ['789.work']
        
        #마.바꾸기(replace)
        # 변수 지정 없는 replace는 함수 적용 후 바로 이전 상태로 회귀, 변형된 상태가 계속되기 원하면 변수 지정 필수
        a='123.ppt'
        b='456.excel'
        c='789.word'
        ##
        a.replace('ppt', 'PPT')
        '123.PPT'
        print(a)
        '123.ppt'
        a_=a.replace('ppt', 'PPT')
        print(a_)
        '123.PPT'

        #바.공백 제거(strip)
        #문자열이 갖고 있는 공백을 제거, strip 함수는 괄호 안에 어느 공백으로 둔다
        a='   123.ppt'
        a.strip()
        '123.ppt'
    
    <9.모듈>
        #가.모듈/패키지
        #함수를 만들어 놓은 모듈, 모듈을 모아놓은 것은 패키지라함
        #많이 쓰는 패키지는 numpy(과학 계산) / pandas(데이터 분석) / matplotlib (시각화) / seaborn (시각화)

        #나.패키지 불러오기
        #import pandas 판다스 패키지 불러오기
        #from pandas import Dataframe 판다스 안에 있는 데이터 프레임 모듈 불러오기

        #다.패키지 별칭 붙이기
        #import pandas as pd
        pd.Dataframe()
        numpy=np
        pandas=pd
        matplotlib=_plt
        seaborn=sns



