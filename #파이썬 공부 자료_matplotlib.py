#파이썬 공부 자료_matplotlib

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
mpl.rcParams['font.family']='Apple SD Gothic Neo'
plt.rcParams["figure.figsize"] = (12, 9)

<그래프 밑그림 그리기>
    <1.틀잡기>
        #가.단일 그래프
        data=np.arange(1, 100)
        plt.plot(data) #그래프 함수 plot
        plt.show() #그래프 소환 show 
        
        #나.다중 그래프
        data1=np.arange(1, 100) #데이터 1
        plt.plot(data1)
        data2=np.arange(20, 50)
        plt.plot(data2) #데이터 2
        plt.show()
        
        #다.다중 그래프 따로 그리기
        #figure 사용하기
        data1=np.arange(1, 100) #데이터 1
        plt.plot(data1)
        data2=np.arange(20, 50)
        plt.figure() #그래프 따로 그리는 함수
        plt.plot(data2) #데이터 2
        plt.show()
        
        #subplot(row,column,index) 사용하기
        data1=np.arange(1, 100) #데이터 1
        plt.subplot(2,1,1) #211 콤마 뺴고도 가능
        plt.plot(data1)
        data2=np.arange(20, 50)
        plt.subplot(2,1,2) #212 콤마 뺴고도 가능
        plt.plot(data2) #데이터 2
        plt.show()
        
        #그래프 숫자가 많아지면 subplots
        data1=np.arange(1, 50)
        data2=np.arange(3, 50)
        data3=np.arange(10,50)
        
        fig, axes = plt.subplots(3,2) #subplots를 쓸 때는 행과 열 둘다 2개 이상일 경우 사용 가능
        
        axes[0,0].plot(data1)
        axes[1,0].plot(data2)
        axes[2,0].plot(data3)
        axes[0,1].plot(data1)
        axes[1,1].plot(data2)
        axes[2,1].plot(data3)
        
        plt.show()
    
    <2.그레프 옵션>
        plt.plot(np.arange(10), np.arange(10)*2, marker='o', linestyle='-', color='b', alpha=0.1)
        plt.plot(np.arange(10), np.arange(10)*2 - 10, marker='v', linestyle='--', color='c', alpha=0.5 )
        plt.plot(np.arange(10), np.arange(10)*2 - 20, marker='+', linestyle='-.', color='y' alpha=0.7)
        plt.plot(np.arange(10), np.arange(10)*2 - 30, marker='*', linestyle=':', color='r', alpha=1.0)
        #marker는 선 중간 찍히는 도트 모양
        #linestyle은 선 종류
        #color 는 선 컬러
        #alpha는 선의 투명도로 0.1 --> 1.0 갈수록 진해진다
        
        # 타이틀 & font 설정
        plt.title('그리드 설정 예제', fontsize=20)

        # X축 & Y축 Label 설정
        plt.xlabel('X축', fontsize=20)
        plt.ylabel('Y축', fontsize=20)

        # X tick, Y tick 설정, 축 레이블 값
        plt.xticks(rotation=90) rotation은 축 레이블 값 기울기
        plt.yticks(rotation=30)

        # legend 설정 범례
        plt.legend(['10 * 2', '10 ** 2', 'log'], fontsize=15)

        # x, y limit 설정, 최대/최소값
        plt.xlim(0, 5)
        plt.ylim(0.5, 10)

        # grid 옵션 추가
        plt.grid()

        plt.show()    
        


