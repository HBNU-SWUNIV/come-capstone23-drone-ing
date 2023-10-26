# 한밭대학교 컴퓨터공학과 Drone-ing팀

**팀 구성**
- 20181616 박상기 
- 20181609 고유진
- 20181628 이동헌

## <u>Drone-ing</u> Project Background
- ### 필요성
  ![image](https://github.com/HBNU-SWUNIV/come-capstone23-drone-ing/assets/100181494/a1741f92-c0dc-47fc-a70c-7fc39825f900)

  - Edge Computing 기술을 활용하여 응답시간을 개선하고 대역폭을 절약하기 위해 단말과 가까운 거리에 컴퓨팅 능력이 있는 연산 장치를 도입하는 분산 컴퓨팅 패러다임을 도입하여 트래픽의 양을 줄일 수 있다.

  ![image](https://github.com/HBNU-SWUNIV/come-capstone23-drone-ing/assets/100181494/50fd6a4b-ce6d-4df8-ba0d-b7eba9e2e552)

  - 우크라이나와 러시아 전쟁, 튀르키예 지진 등 전쟁이나 자연재해와 같은 재난이 발생하면 기존 네트워크 인프라가 무너져 해당 지역의 비상 통신에 막대한 문제가 발생할 수 있다. 이러한 상황에서 무선 연결을 제공하고 데이터나 정보를 빠르게 전달 가능한 보조 네트워크가 필요하다. 이 점을 무인 항공기인 드론을 통해 높은 이동성과 유연성을 바탕으로 해당 상황에 적합하다.
  
## System Design
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white"> <img src="https://img.shields.io/badge/ROS-22314E?style=for-the-badge&logo=ROS&logoColor=white"> <img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=Ubuntu&logoColor=white">

![image](https://github.com/HBNU-SWUNIV/come-capstone23-drone-ing/assets/100181494/08e811b1-1941-48d8-ac60-9eb9aee806a9)

  - ### System Requirements
    - Ubuntu 18.04
    - Python 3.12
    - Jetson Nano
    - ROS Melodic
      
  - ### ROS 기반의 통신 방법

    ![image](https://github.com/HBNU-SWUNIV/come-capstone23-drone-ing/assets/100181494/b5ed483e-7cb8-4d03-af96-40d8beb19523)

      - ROS 시스템의 데이터 통신은 토픽(Topic), 서비스(Service), 액션(Action) 등의 형태를 가짐

      - 연속적인 데이터 송수신이 가능한 토픽 형태의 통신을 활용

      - 실질적인 데이터 전송이 ROS Master를 거치지 않고 노드 간에 직접 이루어짐

      -> ROS는 효율적이고 확장 가능한 통신이 가능하기 때문에 ROS 기반의 통신 방법을 사용
    
    
## Case Study
  - A. Guillen-Perez, R. Sanchez-Iborra, M. -D. Cano, J. C. Sanchez-Aarnoutse and J. Garcia-Haro, "WiFi networks on drones," 2016 ITU Kaleidoscope: ICTs for a Sustainable World (ITU WT), Bangkok, Thailand, 2016, pp. 1-8, doi: 10.1109/ITU-WT.2016.7805730

      - 드론을 이용한 공중 WIFI 네트워크를 배치하기 위해 두가지의 WIFI 모드(2.4GHz, 5GHz)를 비교하는 실험 및 연구

  - D. Wu, X. Sun and N. Ansari, "A Cooperative Drone Assisted Mobile Access Network for Disaster Emergency Communications," 2019 IEEE Global Communications Conference (GLOBECOM), Waikoloa, HI, USA, 2019, pp. 1-6, doi: 10.1109/GLOBECOM38437.2019.9013813.

      - 모바일 사용자가 근처 기지국이 없을 경우 드론 탑재 기지국을 통해 기지국와 통신하는 알고리즘 설계
  
## Conclusion
  - 데이터 처리시간 단축으로 저지연 통신 가능이 가능해진다.
  - 드론의 유연성과 이동성으로 광범위하고 빠르게 데이터 통신이 가능해진다.
  - 네트워크 인프라가 구축되지 않은 지역이나 재난현장, 전시상황에서 데이터 통신이 가능해진다.
  
## Project Outcome
- ### 2023년도 한국통신학회 하계 종합 학술 발표회
    - 드론 네트워크에서 ROS 기반의 무선통신 성능평가
