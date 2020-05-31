# e-루리 도우미

강원대학교 e-루리를 크롤링해 강의와 과제 진행 상황을 한눈에 확인하는 애플리케이션입니다.

## 설명
Crawler와 Frontend 두 부분으로 나뉩니다. Crawler는 파이썬으로 개발되었고 Frontend는 Electron + vue.js로 개발되었습니다. 프로세스 간 HTTP 통신을 이용해 두 파트가 상호작용합니다.

## 설치
### Crawler
Crawler는 아래와 같은 라이브러리를 설치해야 실행 할 수 있습니다.

* flask_restful
* flask_cors
* beautifulsoup4
* requests

### Frontend
아래 명령어로 설치하여 디버그 모드로 실행할 수 있습니다.
```sh
npm install
npm run dev
```
아래 명령어로 빌드할 수 있습니다.
```sh
npm run build
```

Crawler가 선행적으로 켜져 있어야 정상적으로 작동합니다.