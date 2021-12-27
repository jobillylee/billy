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
        numpy.array([1,2,3,4],[5,6,7,8],[9,10,11,12])

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
