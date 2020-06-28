# KCB_financial_style
### Dacon - KCB 금융스타일 시각화 분석
## 개요
* DACON의 KCB 금융 스타일 시각화 경진대회(종료,제주part)의 데이터를 활용한 분석&시각화


## requirements
* pip install -r requirements.txt


## path
* root : User\data (folder)


## 데이터출처,설명
* __([Dacon copy](https://dacon.io/competitions/official/82407/data/))__ 모든 값의 단위는 (원) 이고, 필드를 보유한 사람끼리의 평균(※ 즉 0을 포함하지 않은 평균) 
* 일부 통계 값을 조정하여 제공하였기 때문에 수치의 오류가 있어보일 수 있으나, 해당 수치를 기준으로 시각화 결과물을 제작. 
* KCB 정책 상 대출 카테고리 및 상환 유형 등에 대해 필드를 일부 제거하여 대출 총합과 해당 카테고리들 합이 다를 수 있음. 
* 2016년 1월 10대 남녀의 대출 관련 수치가 전체적으로 오류가 있는 것으로 확인됨. (KCB 스코어 변경이슈 관련) 해당 컬럼은 되도록이면 무시

* jeju_financial_life_data.csv : 지역 거주지(제주도) 금융라이프 데이터
제주도의 우편번호 단위 지역민의 금융생활 통계 데이터
우편번호 단위 별, 거주지 블록 별 소득 비교, 채무 현황, 다양한 컬럼을 활용하여 인사이트를 발굴할 수 있음.
    
    <details>
    <summary> Details </summary>

        zip_cd 신우편번호 신우편번호  지역: 제주특별자치도
        year_month 기준월 해당 정보 자료의 시점기준 정보   
        x_axis 좌표 해당 우편번호의 경도   
        y_axis 좌표 해당 우편번호의 위도   
        sex 성별 1: 남성, 2: 여성   
        age 연령대 5세 구간(24: 24세이하, 29: 25-29세, 34: 30-34세, …. , 74: 70-74세, 79: 75-79세, 99: 80세이상)   
        job_majorc 직업군별 비율-대기업 고객군의 직업군별 비율 : 대기업 ratio 범위 : 0~1
        job_smallc 직업군별 비율-중소기업 고객군의 직업군별 비율 : 중소기업 ratio 범위 : 0~1
        job_public 직업군별 비율-공기업 고객군의 직업군별 비율 : 공기업 ratio 범위 : 0~1
        job_profession 직업군별 비율-전문직 고객군의 직업군별 비율 : 전문직 ratio 범위 : 0~1
        job_self 직업군별 비율-자영업 고객군의 직업군별 비율 : 자영업 ratio 범위 : 0~1
        job_none 직업군별 비율-무직 고객군의 직업군별 비율 : 무직 ratio 범위 : 0~1
        job_other 직업분별 비율-기타 고객군의 직업군별 비율 : 판단불가 ratio 범위 : 0~1
        avg_income 평균연소득 고객군별 평균 KCB 결정연소득 numeric 단위 : 원
        med_income 중위연소득 고객군별 KCB 결정연소득의 중위수(median)값 numeric 단위 : 원
        avg_spend 평균소비액 고객군별 3개월 평균 KCB 총카드이용금액 numeric 단위 : 원
        avg_foreign_spend 평균해외소비액 고객군별 3개월 평균 KCB 총 카드해외이용금액 numeric 단위 : 원
        avg_debt 채무 평균보유액 고객군별 채무보유자의 평균 KCB 총대출잔액 numeric 단위 : 원
        avg_debt_credit 채무 평균보유액-신용대출 고객군별 채무보유자의 평균 KCB 신용대출잔액 numeric 단위 : 원
        avg_debt_noneb 채무 평균보유액-비은행대출 고객군별 채무보유자의 평균 KCB 비은행권대출잔액 numeric 단위 : 원
        avg_debt_mortgage 채무 평균보유액-주택담보대출 고객군별 채무보유자의 평균 KCB 주택담보대출잔액 numeric 단위 : 원
        avg_debt_deposit 채무 평균보유액-예적금유가증권담보대출 고객군별 채무보유자의 평균 KCB 예적금 또는 유가증권 담보대출 잔액 numeric 단위 : 원
        avg_debt_collateral 채무 평균보유액-물건담보대출 고객군별 채무보유자의 평균 KCB 물건담보(주거용 및 비주거용 부동산, 자동차 등) 대출 잔액 numeric 단위 : 원
        avg_credit_rat 평균관리지수 고객군별 신용평균 numeric  
        medium_resid_rat 중대형이상 거주비율 고객군의 중대형 평형 거주비율(30평 이상) (-999,999: 부동산가격이 없는경우) ratio 범위 : 0~1
        large_resid_rat 대형 거주비율 고객군의 대형 평형 거주비율(40평 이상) (-999,999: 부동산가격이 없는경우) ratio 범위 : 0~1
        vehicle_own_rat 중대형 차량소유비율 고객군별 중대형 차량소유비율 ratio 범위 : 0~1 

    <details>


## Report

![이미지](https://github.com/kdj6394/KCB_financial_style/blob/master/img/job_ratio%20by%20job.png?raw=true)

* 성별에 따른 직업비율 변수확인결과 대기업,중소기업,공공기업,자영업의 경우 남성의 비율이 더 높았으며 나머지(전문직,무직,기타)의 비율은 여성이 더 높은것을 확인 할 수 있다.


![이미지](https://github.com/kdj6394/KCB_financial_style/blob/master/img/avg_income.png?raw=true)

* 성별, 나이에 따른 평균수입의 확인결과 남성이 여성보다 더 많은 수입을 가지게 되는것으로 나타난다. 
* 남성 수입의 최솟값과 최대값은 __24세 구간의 평균 23,525,962 원 이며 54세 구간의 평균 50,120,122 원 이다.__
* 여성 수입의 최솟값과 최댓값은 __24세 구간의 평균 21,533,861 원 이며 49세 구간의 평균 35,023,096 원 이다.__


![이미지](https://github.com/kdj6394/KCB_financial_style/blob/master/img/avg_spend.png?raw=true)

* 성별,나이에 따른 평균지출의 확인결과 34세 구간 이전까지 여성의 평균 지출액이 더 많다. 하지만 34세 구간의 이후는 남성의 평균 지출액이 더 많은것으로 나타났다.
* 두 성별의 평균지출의 최댓값은 남성과 여성 모두 44세 구간이며 남성은 7,451,906 원 이며 여성은 6,614,831 원 이다.

* 두 성별 모두 최댓값을 가지는 44세 구간이후 평균 지출액이 감소하는것으로 나타났다.


![이미지](https://github.com/kdj6394/KCB_financial_style/blob/master/img/avg_foreign_spend.png?raw=true)

* 두성별간 3개월 내의 평균 카드해외지출액이다.
* 남성의 경우 29세~44세 구간까지 높은 소비를 보여주다 하락하며 여성의 경우 29세에서 34세 이후에 하락하는 모습을 보인다.

![이미지](https://github.com/kdj6394/KCB_financial_style/blob/master/img/avg_debt.png?raw=true)

* 두성별간 채무 평균 보유액이다. 채무평균액 역시 남성이 더 높게 나타나며 두 성별모두 24세부터 44세까지 급격히 증가하는 모습을 보인다.


![이미지](https://github.com/kdj6394/KCB_financial_style/blob/master/img/avg_all.png?raw=true)

* 모든그래프를 확인해본결과 비슷한 개형을 가진다.
* 39세를 기점으로 69세 까지가 채무,수입,지출이 모두 큰값을 가진다.


![이미지](https://github.com/kdj6394/KCB_financial_style/blob/master/img/medium_resid_rat.png?raw=true)

* 중대형이상 거주비율(30평이상)의 그래프이다.
* 부동산가격이 없는경우(-999,999)를 제외한 그래프이며 두성별 모두 69세를 기점으로 하락이 시작된다.

![이미지](https://github.com/kdj6394/KCB_financial_style/blob/master/img/large_resid_rat.png?raw=true)

* 대형 거주비율(40평이상)의 그래프이다.
* 부동산가격이 없는경우(-999,999)를 제외한 그래프이며 중대형과는 정반대의 형태를 가진다.
* 남성의 경우 54세에서 64세의 구간 급격히 증가하며 여성의 경우 64세에서 69세 구간 급격히 증가한다. 

![이미지](https://github.com/kdj6394/KCB_financial_style/blob/master/img/vehicle_own_rat.png?raw=true)

* 중대형 차량소유비율 그래프이다.
* 두성병 모두 비슷한 개형을 가지고 있으며 24세 부터 34세까지의 구간에서 소유비율이 급격히 증가한다.
* 두성별 모두 59세를 기점으로 급격히 하락하는 모습이 보인다.

![이미지](https://github.com/kdj6394/KCB_financial_style/blob/master/img/all_coreelation.png?raw=true)

