# 소개
Django 연습을 위한 블로그 호스팅 프로젝트입니다.

한번에 완성하기 보다는 조금씩 조금씩 완성해 나갈 예정입니다.

# 빌드 방법

## 1. Python으로 직접 실행

### Python 3.9.2 버전 준비
Python으로 local 환경에서 직접 실행하려면 다음 준비물이 필요합니다.
- Python 3.9.2

[Pyenv](https://github.com/pyenv/pyenv)를 사용하시는 분이라면 3.9.2 버전을 설치하시고 이 프로젝터 폴더로 진입할 경우 `.python-version` 파일에 의해 3.9.2로 자동으로 Python 버전이 결정될 것입니다.
그렇지 않다면 Python을 3.9.2로 빌드해 사용해주세요.

### Python pacakage 설치
다음 명령어를 사용해 필요한 Python pacakage를 설치합니다.

`$ python3 -m pip install -r requirements.txt`

### 실행
프로젝트 폴더의 최상단에서 다음 명령어를 실행합니다. (아직 호스팅 단계는 아니기 때문에 다음 명령어를 사용합니다)

`$ python3 manage.py runserver`

그럼 이제 웹사이트를 `localhost:8000`에서 접근가능할 수 있습니다.

## 2. Docker 사용
Docker를 사용하신다면 포함된 `Dockerfile`과 `docker-compose.yml` 파일을 사용해 빌드와 실행을 하실 수 있습니다.

### 이미지 빌드
단, `docker-compose.yml`에 이미지 이름이 `django-blog`로 명시되어 있으므로, 이미지 이름은 이대로 해주시면 됩니다.

`$ docker build -t django-blog -f Dockerfile .`

### docker-compose를 사용해 실행
다음 명령어를 사용해 실행하실 수 있습니다.

`$ docker-compose up`