# 🦰 얼굴인식 기술을 이용한 단골고객 주문 프로그램
- 딥러닝 얼굴인식 기능을 활용하여 단골고객에게 메뉴를 추천해주는 프로그램입니다.
- 얼굴인식을 통해 등록된 단골고객의 정보를 활용하도록 구현 했습니다.
- 고객의 구매 LOG 데이터를 활용하여 개인 맞춤형 BEST 메뉴를 추천합니다.
- 기존 스타벅스 메뉴를 활용하여 프로그램을 구현하였습니다.

<br>

## 👀 프로젝트 개요  
- 📆 프로젝트 기간  
  - 2020.09.01  ~ 2020.09.21 (3Weeks)


- 📌 기획 배경
  - 코로나19 상황으로 언택트 일상이 오면서 비대면 서비스 도입의 가속화 
  - 자동 주문을 받는 키오스크, 로봇서빙 등 활용도가 높아지지만 작동방법의 불편함 존재
  - 얼굴인식 기술을 활용하여 빠르고 효율적인 주문 시스템을 구현하기 위하여 제작

<br>
<br>

## 🔧 프로젝트 사용기술
- Python-PyQt5 (Client)
- Python-Flask (Server)

<br>
<br>

##  :rocket: 서비스 흐름도
![K-058](https://user-images.githubusercontent.com/54658745/131123822-c37be11f-c15f-4330-a906-11d25db62c65.png)

![K-057](https://user-images.githubusercontent.com/54658745/131123814-bdbd470e-327c-410d-bfee-6f2a37a49c34.png)


## 📈 사용 알고리즘
### 1️⃣ Deep Learning CNN Face Recognition model 활용
- face recognition 오픈 소스 활용 [GitHub](https://github.com/ageitgey/face_recognition)
- 기존에 저장된 단골고객의 이미지를 활용하여 고객의 ID 찾아내기  

![K-059](https://user-images.githubusercontent.com/54658745/131124583-f082de73-9f01-4def-a060-4c74e7f31a3e.png)
![K-060](https://user-images.githubusercontent.com/54658745/131124589-2bbb8c2a-33ef-4876-8c25-243a8c211c56.png)
![K-061](https://user-images.githubusercontent.com/54658745/131124595-c6ab4c53-a296-478a-bc01-3d8a1fbf8f23.png)
![K-062](https://user-images.githubusercontent.com/54658745/131124601-1e1076f3-fef9-499c-aed2-c5121db301aa.png)
![K-063](https://user-images.githubusercontent.com/54658745/131124606-a3a01702-1d44-4d2f-8ae4-79a8254e43f4.png)

 
### 2️⃣ Machine Learning Recommend - Item-based filtering
- 고객의 주문 데이터를 활용하여 유사한 사용자가 구매한 메뉴를 그룹핑한 후 사용자에게 BEST 메뉴 추천  
![K-064](https://user-images.githubusercontent.com/54658745/131124965-1dd453ab-ceff-451b-b69f-d2dff6a44d88.png)


<br>
<br>


##  ✨ 화면 구성도 및 주요 기능
### 1️⃣ 얼굴인식을 통해 회원 로그인
![K-065](https://user-images.githubusercontent.com/54658745/131125240-e234406f-387d-42d9-a8a6-fa05867b30ad.png)

### 2️⃣ 고객의 구매 데이터 분석을 통해 BEST 메뉴 추천  
![K-066](https://user-images.githubusercontent.com/54658745/131125349-a45564c2-14a6-4abb-ae02-f863093ce497.png)

### 3️⃣ BEST 추천 메뉴 이외에도 다른 메뉴 구매할 수 있도록 구현
![K-067](https://user-images.githubusercontent.com/54658745/131125525-1a12b338-ba82-4b83-a5b7-15874a04bf85.png)
![K-068](https://user-images.githubusercontent.com/54658745/131125571-3f671bff-c002-4005-b6fb-e8517f6d027a.png)

### 4️⃣ 다른 고객에게도 개인 맞춤형 메뉴 추천
![K-069](https://user-images.githubusercontent.com/54658745/131125647-05cfa805-2c92-4dd7-ad71-47481d480d17.png)
![K-070](https://user-images.githubusercontent.com/54658745/131125651-12c90013-498c-417d-aeee-49e157aae9fe.png)

<br>
<br>

## 📝 프로젝트 기대 효과
- 일반 사용자에게 개인 맞춤형 주문 시스템을 통해 간편함 제공
- 디지털 소외계층의 어려운 주문 조작 시스템에 편리성 제공
- 구매 데이터가 많아질수록 성능 좋은 맞춤 서비스 제공 가능
- 추후 연령대, 성별의 추정 모델을 통해 비회원에게도 맞춤 서비스 제공 가능

<br>
<br>

## 🎉 프로젝트 결과
- 2020년도 조선대학교 소프트웨어 경진대회 금상 수상
