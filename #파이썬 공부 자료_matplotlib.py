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
        #가.scatterplot
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
        
        #나.barplot
        #sns에서는 bar/barh 구분이 없다. barplot에서 x,y만 바꿔서 작성하면 된다.
        x = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
        y = [66, 80, 60, 50, 80, 10]
        sns.barplot(x,y,alpha=0.7,palette='YlGnBu')
        plt.grid()
        plt.title('연습삼아 또 해보자')
        plt.xlabel('과목')
        plt.show()
        
        #그래프를 임의로 그려야 하는 경우 matplotilb, 데이터 프래임으로 그려야 하는 경우 seaborn
        titanic = sns.load_dataset('titanic')
        titanic.head()
        sns.barplot(x='survived',y='age',hue='pclass',data=titanic, palette='muted')
        plt.show()
        #에를 들어 sns.barplot(기간,매출,hue=시즌/비시즌,)
        
        #다.lineplot
        #sns.set_style('') 통해 그래프 백그라운드 컬러 및 형태를 지정할 수 있다.
        #whitegrid(흰바탕 격자) darkgrid(회색바탕 격자), white(흰색 무지), dark(회색 무지)
        x = np.arange(0, 10, 0.1)
        y_1 = 1 + np.sin(x)
        y_2 = 1 + np.cos(x)

        sns.set_style('darkgrid')

        sns.lineplot(x,y_1,markers="v", linestyle='-.',palette="muted",label='sin')
        sns.lineplot(x,y_2,markers="o", linestyle='--',palette="muted",label='cos')

        plt.title('sin cos 그래프')
        plt.ylabel('value')

        plt.show()
        
        #라.areaplot
        #seaborn에서는 areaplot을 지원하지 않는다.
        x = np.arange(1,21)
        y =  np.random.randint(low=5, high=10, size=20)
        plt.fill_between(x, y, color='g', alpha=0.5)
        sns.lineplot(x,y,color='g')
        plt.show()
        
        #마.distplot (전 histplot)
        #seaborn에서는 hist가 아닌, distplot으로 명령어 사용
        #메소드 사용하여 빈도(빈도수분포와 밀도 표현 가능)
        #도수 : hist='True' / 밀도 : kde='True' / 가로 그래프 : vertical='True' / 누적분포 : cumulative='True'
        #밀도 그래프에서 도수를 함께 표헌한 그래프(rugplot) : rug='True'
        N = 100000
        bins = 30
        x = np.random.randn(N)
        sns.distplot(x,bins=bins,kde=True,hist=True,vertical=False)
        plt.show()
        
        #바.chartplot
        #seaborn에서는 chartplot는 지원하지 않는다. 
        #chartplot은 별도의 공부가 필요
        
        #사.countplot
        #첫번째 인자의 수를 카운트 하는 그래프,y축을 별도로 지정하지 않는다. 
        #hue 매소드를 사용해 x축를 세분화 하여 볼 수 있다. 
        #외부 데이터를 가저오는 경우, data=데이터 변수명 을 꼭 지정해 줘야 한다
        plt.figure(figsize=(12,6))
        titanic = sns.load_dataset('titanic')

        plt.subplot(121)
        sns.countplot(x='sex',hue='survived',palette='copper',data=titanic)

        plt.subplot(122)
        sns.countplot(y='sex',hue='survived',palette='copper',data=titanic)

        plt.show()
        
        #아.hitmap
        #hitmap 데이터의 상관관계 또는 두 칼럼간 상관관계를 잘 표현
        tips = sns.load_dataset('tips')

        pivot=tips.pivot_table(index='time',columns='smoker',values='tip')
        sns.heatmap(pivot,data=tips,cmap='Blues',annot=True)
        plt.show()
        #annot=True 데이터 값 표시 여부
        
        titanic = sns.load_dataset('titanic')
        x=titanic.corr() #corr는 correlation의 약어 상관관계를 나타냄
        sns.heatmap(x,annot=True,cmap='YlGnBu')

        plt.show()
        
        #자.pairplot 
        #데이터 내 다양한 인자를 인식, 숫자열에 대한 분포를 다양한 그래프로 한번에 보여주는 그래프 
        sns.pairplot(tips, hue='size',palette='rainbow',height=5)
        plt.show()
        
        #차.violinplot
        #컬럼 내 데이터의 비교 분포도 확인할 수 있는 그래프
        #violinplot은 비교 대칭이기 때문에 hue와 split(좌우 둘로 나눠 표시)사용해 분석해야 한다.
        sns.violinplot(tips[total_bill]) #하나의 데이터 분포를 볼 떄 
        #둘 이상의 데이터 분포를 분석할 때 컬럼 하나를 가져오는 게 아닌, x/y를 지정하여 가져온다. 그리고 data=''반드시 붙여야 한다.
        sns.violinplot(x='day',y='total_bill',hue='smoker',split=True,palette='rainbow',data=tips)
        plt.show()
        
        #카.lmplot
        #컬럼 간 선형관계를 확인하는데 용이한 그래프, 튀는 매출, 튀는 숫자를 확인할 수 있다. 
        sns.lmplot(x='total_bill',y='tip',data=tips) #기본 함수
        sns.lmplot(x='total_bill',y='tip',hue='smoker',col='day',col_wrap=2,height=8,data=tips) 
        #hue를 통해 한가지 옵션 추가, col 매소드 활용, 해당 컬럼 기준으로 그래프를 자동으로 나눠서 분석, 
        #col_wrap을 활용해 가로 2개로 지정 
        
        #타.relplot
        #컬럼간 상관관계를 볼 수 있지만 선형 관계를 바로 그리지 못한다. 
        #형태는 scatterplot처럼 두 인자의 관계를 점으로 표현, 도수분포를 나타내는 건 아니다.
        sns.relplot(x='total_bill',y='tip',data)
        sns.relplot(x='total_bill',y='tip',hue='day',col='time',row='sex',height=8,palette='muted',data=tips)
        #기본 xy에서 hue를 구분해 표기하고, time 기준으로 그래프를 col(나누어) 그리되, row(행)은 sex 단위로 나누서 그린다.
        
        #파.jointplot
        #두 컬럼의 관계를 보여주는 scatter와 도수분표 histogram을 동시에 볼 수 있는 그래프
        #jointplot은 col,row 다 안먹힌다. hue는 기본에서는 적용 가능하나 kind와 중복 사용 불가능 하다
        #kind 통해 다양한 그래프를 포현할 수 있다.
        #“scatter(산점도)” | “kde”(밀도분포, 그래프) | “hist”(도수분포,막대) | “hex(6각형 칸)” | “reg”(선형) | “resid(잔차분석)”
        #잔차분석은 실측 - 예측 = 격차를 확인하고자 하는 통계학 
        sns.jointplot(x='total_bill',y='tip',data=tips)
        sns.jointplot(x='total_bill',y='tip',hue='sex',kind='rug',height=8,palette='muted',data=tips)
        #일부 kind와 hue는 함께 사용하지 못한다. ex)resid
        

