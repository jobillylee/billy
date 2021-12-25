#파이썬 공부 자료_기본편_조건문&비교연산(21.12.25)

<기본편>
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

        