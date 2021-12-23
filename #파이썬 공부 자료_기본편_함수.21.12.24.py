#파이썬 공부 자료_기본편_함수(21.12.24)

<기본편>
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




