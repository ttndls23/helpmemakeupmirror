#  메이크업의 Hell에서 너를 구원할게, 헬미 (Help Me Makeup Mirror) 

- Virtual Makeup Smart Mirror of kibwa project 
- 2020 이브와공모전 대상(과학기술정보통신부장관상) 수상작
- https://www.hanium.or.kr/portal/project/awardList.do# 
-![공모전수상페이지](https://user-images.githubusercontent.com/48430781/113113916-c460a980-9245-11eb-91c7-40432c40b645.PNG)

○ 화장을 처음 하는 사람들을 위한 튜토리얼을 제공해주는 스마트 메이크업 거울
> 사용자의 얼굴을 인식한 후 거울 속에 가상메이크업 투영, 얼굴 부위 영역(눈썹, 아이라인 영역 등)에 점선으로 프레임을 보여주어 따라 하기 쉬운 메이크업 튜토리얼을 제공함으로써 입문자들의 진입 장벽을 허물 수 있게 도와준다.

○ 자신의 얼굴형, 특징, 톤에 어울리는 메이크업을 추천
> 딥러닝을 통해 얼굴형 데이터 셋을 학습시켜 사용자 얼굴형을 분석한다. 분석 결과에 따라 얼굴형 스타일에 어울리는 메이크업 스타일을 추천해준다. 얼굴 분석 데이터를 이용해 얼굴 톤에 따라 퍼스널 컬러를 추론시켜 피부 톤에 알맞은 색상 스타일 추천에 활용한다.

## 시연영상
https://youtu.be/v81LYKVmSwQ

## 기능
1) AI 얼굴인식
- 데이터 셋을 수집, CNN알고리즘을 통해 모델을 생성 
- 사용자의 얼굴을 인식하여 분석한 피부 톤, 특징, 얼굴형에 어울리는 메이크업을 추천
2) 가상 메이크업 스타일 선택
- 눈썹의 종류(일자형, 아치형), 아이라인의 길이, 아이섀도우의 색깔 등 사용자가 선호하는 조합으로 스타일 제작이 가능
- 테마(계절,상황)별로 완성된 스타일 선택 가능
3) 프레임(Frame)
- 얼굴인식을 통해 사용자가 선택한 가상메이크업 스타일에 따른 맞춤형 프레임을 제공.
- 종류 : 눈썹의 종류(일자형, 아치형), 아이라인의 종류와 길이, 아이섀도우 및 블러셔 영역이 있다.
4) 퍼스널컬러
- 퍼스널 컬러를 진단을 통해 사용자에게 어울리는 톤과 메이크업 스타일을 추천.
- 퍼스널 컬러 톤에 따라 봄 웜톤, 여름 쿨톤, 가을 웜톤, 겨울 쿨톤으로 나뉜다. 

## 사용한 기술 스택
- Python (all SW)
- Figma(client, UI, Prototype 제작)
- PyQt5(GUI 라이브러리)
- Jetson Nano(HW 디바이스)
- opencv, dlib, numpy, scipy (AR 라이브러리)
- CNN (얼굴형 판단 딥러닝 알고리즘) 
- Github/Gitlab (버전관리)

## 구성도
![image](https://user-images.githubusercontent.com/48430781/113004607-b14eca80-91ae-11eb-89e2-25dfbc6955ff.png)

## UI 기획안
![image](https://user-images.githubusercontent.com/48430781/113004717-c75c8b00-91ae-11eb-8930-23187099ba56.png)

## 특징 & 장점
1) 사용자 맞춤형 프레임 및 선택형 프레임 제공
- 사용자의 사진을 기반으로 사용자의 얼굴형을 판단
- 얼굴형에 어울리는 적절한 화장 범위 프레임을 제공 : 쉽게 메이크업을 배우고 익힐 수 있도록 도와줌
- 프레임을 직접 선택할 수 있음 : 다양한 화장법을 시도할 수 있음
2) 퍼스널 컬러 진단 기능 제공
- 직접 가게에 가지 않아도 손쉽게 자신의 퍼스널 컬러를 진단 가능
- 추가 비용이 들지 않기 때문에 퍼스널 컬러 진단과 관련된 금액적 부담을 줄여줌
- 진단된 퍼스널 컬러 결과를 기반으로 사용자에게 어울리는 색상을 추천&가상 메이크업해줌으로써 화장 고민을 줄여줌

## 결과물 상세 이미지
![image](https://user-images.githubusercontent.com/48430781/113008091-b2cdc200-91b1-11eb-9a50-06bdf4ab116c.png)
![image](https://user-images.githubusercontent.com/48430781/113008100-b4978580-91b1-11eb-9c0c-758a22d38396.png)
![image](https://user-images.githubusercontent.com/48430781/113008110-b5c8b280-91b1-11eb-9b01-6b70fc18beda.png)



