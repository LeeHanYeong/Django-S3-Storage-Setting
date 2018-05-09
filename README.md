# django-storages with S3 and django-sass-processor


## Requirements

### Environments

- Python (3.6)

### Python packages 

- django
- [django-storages](https://github.com/jschneier/django-storages)
- [django-sass-processor](https://github.com/jrief/django-sass-processor)
- [django-compressor](https://github.com/django-compressor/django-compressor)
- libsass

### Secret JSON file

`secrets.json (in root directory)`

```json
{
  "AWS_ACCESS_KEY_ID": "",
  "AWS_SECRET_ACCESS_KEY": "",
  "AWS_STORAGE_BUCKET_NAME": ""
}
```

## Installation

```
# Using pipenv
pipenv sync
```
or

```
# Using pip
pip install -r requirements.txt
```

## Sass파일 설정

템플릿에서 `sass_src` 템플릿 태그 사용

```django
<link href="{% sass_src 'scss/example.scss' %}" rel="stylesheet" type="text/css">
```

## 배포 시 사용법

아래 명령어들을 배포 과정에 추가한다

```
# Scss파일을 컴파일해서 해당 파일의 위치에 css파일을 생성
# .gitignore에 해당 패턴의 css파일 목록 무시하도록 작성해야 함
python manage.py compilescss

# 정적파일 경로에 있으므로 명령어를 이용해 S3로 업로드
python manage.py collectstatic 
```

S3에 파일이 올라가 있다면, `libsass`와 `django-compressor`는 production환경의 애플리케이션에는 설치되어 있지 않아도 됨. (`sass_src`태그는 단순히 파일 위치만을 참조) <- 확인 필요


## 개발과정에서 사용법

`libsass`와 `django-compressor`가 `STATIC_ROOT`를 통해 파일을 제공함

`DEFAULT_FILE_STORAGE`와 `STATICFILES_STORAGE`의 설정은 로컬 컴파일을 사용할 경우, `staticfiles`의 `FileSystemStorage`를 사용하도록 한다.
