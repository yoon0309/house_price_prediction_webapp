# Section3 : 미국 시애틀 KingCountry 지역의 집 값 예측 웹사이트 


### 1. 데이터 셋 

미국 시애틀 KingCountry 지역의 주택 판매 가격 데이터 셋(https://www.kaggle.com/datasets/harlfoxem/housesalesprediction) 으로

Column명은 id, date, price, bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, grade, sqft_above, sqft_basement, yr_built, yr_renovated, zipcode, lat, long, sqft_living15, sqft_lot15로 구성되어있습니다.  

컬럼의 자세한 정보는 
- id   구매자 id 
- date	거래 날짜	 
- price 	주택 가격, Target	 
- bedrooms 침실 개수	 
- bathrooms	욕실 개수	 
- sqft_living	집 면적	 
- sqft_lot	토지 면적	 
- floorsTotal	집의 측	 
- waterfront	강변전망 여부	 
- view	전망이 얼마나 좋은지 0 에서 4 로 평가	 
- condition	전반적으로 집 상태가 얼마나 좋은지를 나타내는지표로1 (매우 좋지 않음) 에서 5 (매우 좋음)로 평가
- grade	King Country 평가 시스템에 따른 전반적인 집의 등급으로 Grads 1 (협소, 정비되지 않음) - Grade 13 (큰 규모, 상태 좋음)- sqft_above	지하로 부터의 높이	 
- sqft_basement	지상으로 부터의 높이	 
- yr_built	건축 년도	 
- yr_renovated	리모델링 년도	 
- zipcode	우편번호	 
- lat	위도	 
- long	경도	 
- sqft_living15	근방 15 가구 정도를 위한 생활 공간의 면적

  
으로 구성되어 있습니다.

### 2. 프로젝트에서 풀고자 하는 문제 (문제인식, 문제 정의, 가설)


미국 시애틀 Kingcountry 지역의 Bedroom(침실 수), bathroom(화장실의 수), floors(층수), yr-bulit(지어진 년도)를 이용한 집값 예측을 통해 합리적으로 집을 구매할 수 있다.

 

### 3. 프로젝트 진행과정  

네이버 부동산을 기준으로 거래방식, 가격대, 면적, 사용승인일, 세대수, 층수, 방/욕실 수, 방향, 융자금, 기타옵션이라는 선택지가 있는 것을 확인하였습니다.  

사람들의 집 선택 기준을 4가지로 축소하여 최종적으로 bedrooms (침실 개수), bathrooms(욕실 개수), floors(층수), yr_built(건축 년도) 컬럼을 이용하였습니다. 

선형회귀모델을 이용한 집값 예측하는 모델을 만든 후 picking을 통하여 모델을 저장하고 flask를 통하여 웹사이트 연결을 하였습니다. 

또한 MongoDB를 통하여 DB에 저장 후 mongodb chart, google data studio를 통한 대시 보드 제작하였습니다. 



### 4. 문제상황 해결과정(분석기법, 모델 등)


4가지 컬럼(bedrooms, bathrooms, floors, yr_built)을 통하여 선형회귀모델을 만들었습니다.
다중회귀분석은여러 개의 독립변수(x)를 가지고 종속변수(y)를 예측하기 위한 회귀 모형으로 

다중 선형회귀분석의 일반식은 
![img1 daumcdn](https://github.com/yoon0309/house_price_prediction_webapp/assets/102473586/b726f80e-163c-43c3-9857-c83f50a44d7d)
으로 구성되어 있다. 

일반식의 설명으로는 b1 b2.. 를 편 회귀 계수(Partial regression coefficient), 계수를 통해 설명변수 x1이 종속변수에 대한 영향력을 나타낸다. 

또한, 단순회귀와 마찬가지로 계수는 최소제곱법를 통해 편미분하여 계수를 추정한다. 

다중선형회귀분석 시 유의할 점은 독립변수(설명변수)들끼리의 상관관계가 높으면 다중공선성 문제가 나타날 수 있다. 


Database로 사용된 MongoDB는 NoSQL의 한 종류를 사용하였다. 


### 5. 결과정리


 


### 6. 한계점 및 해결방안  

- 집 값 예측 모델의 선형회귀 모델 구축 전, 컬럼 선정시에 집 구매 선택 기준을 컬럼별로 상관계수를 구하여 가격에 어떤 컬럼이 영향을 주는지 살필 수 있는 지표가 되었을 것 같아서 아쉬움이 남습니다. 
- heroku 연결을 하여 타인이 접근할 수 있는 환경을 만들었으면 더 좋았을 것이라는 생각이 듭니다. 
- mongoDB 외의 다른 Database 연결 시도를 해보고 싶다는 생각이 들었습니다.


### 7. 출처 
https://value-error.tistory.com/26


https://jaehoney.tistory.com/314
