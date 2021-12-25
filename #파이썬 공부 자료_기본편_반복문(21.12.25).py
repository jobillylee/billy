#파이썬 공부 자료_기본편_반복문(21.12.25)

<기본편>
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

        #나.짝수만 출력
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
        

