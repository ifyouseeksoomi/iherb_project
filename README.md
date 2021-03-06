# iherb_project

## '목욕 & 퍼스널 케어' 제품 리스트 scraping
![스크린샷 2021-05-30 오후 10 46 49](https://user-images.githubusercontent.com/59601700/120106653-ec627f80-c198-11eb-8358-95a4084798df.png)

- i-herb에서 취급하는 제품 중 약 총 5000개에 달하는 **목욕 & 퍼스널 케어 제품**을 scrap
- 제품 리스트 페이지에서 보여지는 정보만 취급
- scrap 해온 정보를 저장한 DB 테이블 상세
<img width="365" alt="스크린샷 2021-05-30 오후 6 44 57" src="https://user-images.githubusercontent.com/59601700/120099572-228f0780-c177-11eb-90b9-29c65357d093.png">

- csv 파일 preview
![스크린샷 2021-05-30 오후 10 48 52](https://user-images.githubusercontent.com/59601700/120106734-35b2cf00-c199-11eb-9bfe-ca1015de07c2.png)

<br>

## Built with
- Python, Django
- BeautifulSoup
- Mysql

## Released with
- AWS EC2, RDS
- gunicorn

<br> 

## Clone & runserver Manual
1. 해당 프로젝트를 클론 받을 디렉토리 생성 (ex. iherb_hwangsoomi)
2. 디렉토리 내에서 `git init` 
3. 디렉토리 내에서 `git clone https://github.com/ifyouseeksoomi/iherb_project.git` (주소는 아래 사진을 참조)
![image](https://user-images.githubusercontent.com/59601700/120460416-118f0200-c3d4-11eb-9767-27a2d039add0.png)
4. 이후 디렉토리(1번에서 만든) 내 프로젝트 clone 완료 (프로젝트 명 : iherb)
5. '1번에서 만든 디렉토리'/iherb(터미널에서 ls 명령 시, `manage.py`가 보이는 뎁스)에서 `python manage.py runserver` 시 서버 on
6. 서버 실행 시, `localhost:8000/'url'`로 각각의 API 호출 및 확인 가능

