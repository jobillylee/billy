#파이썬 공부 자료_numpy(21.12.27)

<numpy>
    <01.array>
        #가.array 뜻
        #array는 여러 값들의 그룹, 배열이라 명함
        #1차원 배열 1/2/3/4
        numpy.array([1,2,3,4])
        #2차원 배열
        1/2/3/4
        5/6/7/8
        9/10/11/12
        numpy.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

        #나. ndarray = n dimension array = n차원 배열
        #shape = 배열의 차원을 표시
        #1차원 배열 1/2/3/4 = shape:(4,)
        #2차원 배열
        1/2/3/4
        5/6/7/8
        9/10/11/12
        shape:(3,4)
        #axis = 배열의 기준이 되는 축
        #1차원 배열 1/2/3/4 = shape:(4,) = axis0
        #shape:(3,4) = axis0,1
    
    <2.numpy 기초>
        #가.numpy import
        import numpy as np #as 사용을 습관화 드리는 연습 필요
        arr_1=[[1,2,3,4],[5,6,7,8]] # shape 별로 괄호를 반드시 추가해 줘야 함
        arr=np.array(arr_1) #np 모듈을 활용해 arr_1 list 값을 arr 이라는 변수에 배열 형태로 저장 
        arr
        array([[1,2,3,4],[5,6,7,8]])
        arr.shape
        (2, 5)

        #나.array data type
        #array는 list와 달리 데이터 타입을 한가지로만 가져갈 수 있다
        mylist=[12,1.3,'마음','123']
        arr_1=np.array(mylist)
        arr_1
        array(['12','1.3','마음','123'])
        ##
        mylist=[12,1.3,'123']
        arr_int=np.array(mylist, dtype=int) 
        arr_int
        array([12,1,123])    
        ##
        arr_float=np.array(mylist, dtype=float)
        arr_float
        array([12.,1.3,123.])
        arr[0]+arr[1]
        13.1
        #int와 float이 함께 있는 list의 경우 array는 float로 통일
        ##
        arr_str=np.array(mylist, dtype=str)
        arr_str
        array(['12','1.3','123'])
        arr_str[0] + arr_str[1]
        121.3
        #int와 str이 함꼐 있는 list의 경우 str으로 통일
    
    <3.index>
        #가.슬라이스
        #배열 내 원하는 위치 값을 지정하여 색인
        arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
        arr1[0]
        array[1,2,3]
        arr1[0,0]
        array([1])
        arr1[2,1]
        array([5])
        #배열 내 범위를 지정해서 색인 가능
        #(n번째 이상:n번째 미만)
        arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
        arr1[:,2] #행은 0이상 열은 2
        array([3],[6],[9])
        arr1[1,:2] #행은 1, 열은 2 미만
        array([4,5])
        arr1[:2,1:] #행 2미만, 열 1 이상
        array([2,3],[5,6])
        arr1[-2:,:-1] #행 -2 이상, 열 -1 미만
        array([4,5],[7,8])
        arr[0,:] #특정 행을 모두 가져오고 싶을 때 
        array([1,2,3])
        arr[:,2] #특정 열을 모두 가져오고 싶을 때 
        array([3,6,9])
        
        #나.fancy index
        #배열 내 특정 범위(구간)의 값이 아닌, 원하는 위치의 값 인덱스
        #fancy는 1차원에서는 변수 지정 인덱스하는게 가능하지만 2차원에서도 가능한데 먼가 어려움 
        arr1=np.array(1,2,3,4,5,6,7,8,9)
        idx=[1,4,8]
        arr1[idx]
        array([2,5,9])
        arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
        idx=[2],[0,2] #행은 2, 열은 0, 2번째를 인덱스
        arr1[idx]
        array([7,9])
        arr1[:,[0,2]] #행은 전체, 열은 0, 2번째를 인덱스
        array([[1,4,5],[3,6,9]])

        #다.참 거짓 인덱스 boolean
        #블론 함수는 참 거짓을 바로 넣는 것 보단, 조건에 맞는 수를 true로 보고 인덱스하는 방식으로 사용
        arr = np.array([1, 2, 3, 4, 5, 6, 7])
        myTrueFalse = [True, False, True, True, True, True, True]
        arr[mytrueFalse]
        array([1, 3, 4, 5, 6, 7])
        ## 2차 배열은
        arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        arr2d>2 #arr2d가 2보다 크다고 조건을 주면 아래와 같이 계산
        array([[False, False,  True,  True],[ True,  True,  True,  True],[ True,  True,  True,  True]])
        # 그래서
        arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        arr2d[arr2d>2]
        array([3,4,5,6,7,8,9,10,11,12]) #2차원 이상이지만 조건 색인하면 1차원으로 추출

    <4. arange, range>
        #arange는 np의 모듈, range는 파이썬 함수
        #가.arange는 array를 손쉽게 만들 때 사용 가능
        #arange는 (start,stop,step) 으로 배열 생성 가능
        arr1=np.arange(1,6,2)
        array([1,3,5])
        #start, stop, step 인자를 지정하면 순서와 관계없이 지정 가능
        arr1=np.arange(stop=6,step=2,start=1)
        array([1,3,5])

        #나.range는 범위를 지정해 주는 함수
        #range는 for문과 주로 함께 사용
        for i in range(1,4):
            if i%2==0:
                continue
            print(i)
        1
        3

    <sort 정렬>
        #가.sort 배열을 오름/내림차순으로 정열할 때 sort 함수 사용
        arr=np.array([1, 10, 5, 8, 2, 4, 3, 6, 8, 7, 9])
        np.sort(arr) #함수를 진행하면 바로 오름차순으로 정열되지만, 저장되지 않는다
        array([ 1,  2,  3,  4,  5,  6,  7,  8,  8,  9, 10])
        arr
        array([1, 10, 5, 8, 2, 4, 3, 6, 8, 7, 9])
        
        arr.sort() # 함수를 진행하면 오름차순으로 정렬되며, 저장 된다
        array([ 1,  2,  3,  4,  5,  6,  7,  8,  8,  9, 10])
        arr
        array([ 1,  2,  3,  4,  5,  6,  7,  8,  8,  9, 10])

        arr2=np.sort(arr) #변수를 지정한 후 정렬하면, 정렬값이 저장된다
        arr2
        array([ 1,  2,  3,  4,  5,  6,  7,  8,  8,  9, 10])

        #나. 오름차순 / 내림차순
        #sort함수는 기본적으로 오름차순으로 정리됨
        #내림차순으로 정리하고 싶을 때는 [::-1] 사용
        np.sort(arr)[::-1]

        #다.2차원 배열의 정렬
        #2차원 배열은 shape와 axis 파악하는 것이 우선이다
        arr2d = np.array([[5, 6, 7, 8], [4, 3, 2, 1],[10, 9, 12, 11]])
        arr2d.shape
        (3,4)

        #2차원 배열을 열기준으로 정리하고 싶을 때는 다음과 같이 할 수 있다
        np.sort(arr2d, axis=1)
        array([[ 5,  6,  7,  8],[ 1,  2,  3,  4],[ 9, 10, 11, 12]])

        #행기준으로 정렬할 때는 다음과 같다
        np.sort(arr2d, axis=0)
        array([[ 4,  3,  2,  1],[ 5,  6,  7,  8],[10,  9, 12, 11]])

    <argsort>
        #sort는 배열 정렬 값을 출력, argsort 배열 인덱스 값을 출력
        arr2d = np.array([[5, 6, 7, 8],[4, 3, 2, 1],[10, 9, 12, 11]])
        np.sort(arr2d, axis=1)
        array([[5,6,7,8],[1,2,3,4],[9,10,11,12]])

        np.argsort(arr2d, axis=1)
        array([[0,1,2,3],[3,2,1,0],[1,0,3,2]])
    
    <matrix 행렬>
        #가. 행렬의 규칙
        #행렬은 덧샘, 뺄샘시 shape가 유지 되면서 계산된다
        #곱셈은 계산 방법이 2가지, 일반 포지션간의 곱셈과 행렬 수학의 곱셈 방식(dot) 
        #일반 곱셈은 shape이 동일해야 계산됨, dot은 1:1 매칭 계산이 아닌 행과열이 곱해지는 방식으로 계산된다. shape이 변형된다

        #나.형렬의 덧샘
        #행렬 간의 덧샘 방법은 일반 덧샘과 동일하다
        import numpy as np
        a = np.array([[1, 2, 3], [2, 3, 4]])
        b = np.array([[3, 4, 5], [1, 2, 3]])
        a+b
        array([[4,6,8],[3,5,7]])

        #행렬 안에서 덧셈을 하려면 sum 함수를 이용해야 한다
        a = np.array([[1, 2, 3], [2, 3, 4]])
        np.sum(a, aixs=0)
        array([3,5,7])

        np.sum(a, aixs=1)
        array([6,8])

        #다.행렬의 뺄셈
        import numpy as np
        a = np.array([[1, 2, 3], [2, 3, 4]])
        b = np.array([[3, 4, 5], [1, 2, 3]])
        a-b
        array([[-2,-2,-2],[1,1,1]])

        #라.행렬의 곱셈
        #행렬 포지션 간의 곱셈은 일반 곱셈으로, 행렬 수학 방식에서의 곱셈은 np.dot으로 계산
        import numpy as np
        a = np.array([[1, 2, 3], [2, 3, 4]])
        b = np.array([[3, 4, 5], [1, 2, 3]])
        a*b
        array([[3,8,15],[2,6,12]])

        #dot 함수 사용 방식은 두가지
        np.dot(a,b) #np함수를 사용하는 방법, 이 방법을 추천
        a.dot(b) #일반 파이썬 함수를 사용하는 방법
        import numpy as np
        np.dot(a,b)
        array([[22, 28],[22, 28],[31, 40]])

    <브로드케이트>
        #가.배열 안에서의 사칙연산이 가능하다
        a = np.array([[1, 2, 3],[2, 3, 4]])
        b = np.array([[3, 3, 3],[3, 3, 3]])
        a-1
        array([[0,1,2],[1,2,3]])
        a+1
        array([[2,3,4],[3,4,5]])
        a*2
        array([[2,4,6],[4,6,8]])

        #나.행렬간 사칙연산
        #이 부분은 강의에서 설명이 안된 부분
        #행렬을 shape 했을 때 두 행렬간 행 수는 동일, 열이 한개 일 때 가능 
        a = np.array([[1, 2, 3],[2, 3, 4]])
        b = np.array([[3],[1]]) 
        a+b
        array([4,5,6],[3,4,5])
        a*b
        array([[3,6,9],[2,3,4]])

