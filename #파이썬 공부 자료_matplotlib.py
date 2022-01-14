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
    
    <3.그래프 종류>
        #그래프의 종류는 다음과 같다
        #가.Scatterplot(scatter) = 산점도, 두 변수 간의 관계를 보여주는 대표적인 시각화
        #x,y 간 관계를 그래프화
        plt.scatter(x(x축 구분자), y(x축의 값), s=원의 크기(스칼라or배열), c(cmap)=컬러)
        #date1과 date2의 데이터 수는 반드시 같아야 한다.
        #s와 c 설정에 따라 그래프 효과가 더 높아질 수 있다. 
        
        #나.Barplot(bar), Barhplot(barh) = 막대그래프, bar는 세로, barh 가로 
        #항목별(x)명 값(y)를 그래프화
        plt.bar(x(x축 구분자), y(x축의 값), align='center')
        #align은 'center', 'edge' 두개로 구분
        #bar일 때 width, barh는 height
        #비교 막그래프는 추가 연구 필요
    
        #다.line(plot) = 선 그래프
        plt.plot(x,y) #plot안에 label='' 넣으면 legend만 해도 범례가 나옴
        
        #라.Areaplot(fill_between) = 영역 그래프
        #영역 그래프는 선그래프를 기준으로 영역을 나타내는 그래프
        plt.fill_between( x, y, color="green", alpha=0.3)
        #수평 영역을 채우는 fill_between(x,y)
        #수직 영역을 채우는 fill_betweenx(y,x)
        #다각영역을 채우는 fill(x,y)
        #두 그래프의 영역을 채우는 fill_between'x' (x,y1,y2)
        #areaplot의 선을 강조하고 싶으면 fill_between의 alpha를 주고 plot 그래프를 한번 더 그래면 된다
                
        #Histogram(hist) = 도수분포를 기둥 형태로 나타낸 그래프
        plt.hist(x,bins='')
        #자주쓰는 매소드 : 
        #sharex=True : x축을 공유한다
        #tight_layour=True : fit한 그래프를 생성, 
        #cumulative=True : 누적 그래프 생성 
        #density=True : 밀도로 변환
        
        #piechart(pie) = 원 그래프
        patches, texts, autotexts = plt.pie(sizes,explode=explode,labels=labels,
                                            autopct='%1.1f%%', shadow=True,startangle=90)
        #자주쓰는 매소드 :
        #explode: 파이에서 툭 튀어져 나온 비율
        #autopct: 퍼센트 자동으로 표기
        #shadow: 그림자 표시
        #startangle: 파이를 그리기 시작할 각도
        
        #Box Plot(boxplot) = 상자 그래프
        
    <4.Seabron>
        #가.scatter
        #Seabron은 import 할 때는 as sns를 사용
        #sns에서 scatter 그래프는 sns.scatterplot()으로 명령어를 작성한다
        x = np.random.rand(50)
        y = np.random.rand(50)
        colors = np.arange(50)
        area = x * y * 1000
        sns.scatterplot(x,y,size=area,sizes=(area.min(),area.max()),hue=area,palette='gist_gray')
        plt.show()
        
        #sns에서는 size, sizes를 동시에 지정해 줘야 한다. size는 구체의 크기, sizes는 최대값 최소값 지정
        #hue=area는 컬러 옵션, area 지정으로 동그라미 컬러 삽입
        #palette는 sns 컬러 팔렛트 사용 
        
        #scatterplot 다중 그래프
        plt.figure(figsize=(12,6))

        plt.subplot(131)
        plt.title('alpha=0.9')
        plt.ylabel('Y축')
        sns.scatterplot(x,y,size=area,sizes=(area.min(),area.max()),hue=area,palette='gist_gray',alpha=0.9)

        plt.subplot(132)
        plt.title('alpha=0.6')
        sns.scatterplot(x,y,size=area,sizes=(area.min(),area.max()),hue=area,palette='gist_gray',alpha=0.6)

        plt.subplot(133)
        plt.title('alpha=0.4')
        sns.scatterplot(x,y,size=area,sizes=(area.min(),area.max()),hue=area,palette='gist_gray',alpha=0.4)

        plt.show()
        #sns에서는 size, sizes를 동시에 지정해 줘야 한다. size는 구체의 크기, sizes는 최대값 최소값 지정
        #hue=area는 컬러 옵션, area 지정으로 동그라미 컬러 삽입
        #palette는 sns 컬러 팔렛트 사용 
        
        


