# 📌 To-Do List Web Application

## 📋 프로젝트 소개

이 프로젝트는 Flask를 기반으로 한 **To-Do List 웹 애플리케이션**으로, 사용자가 할 일을 추가, 수정, 삭제, 완료할 수 있도록 설계되었습니다. 로그인 기능을 포함하며, 각 사용자의 개별 할 일 목록을 관리할 수 있습니다.

---
 ────────────────────────────────────────────────────────
  ✅ **프로젝트명**   : To-Do List 웹 애플리케이션  
  🚀 **기능 요약**   : 할 일 관리 (CRUD) 및 마감일 관리
  🔒 **사용자 인증** : Flask-Login 기반 회원 시스템 
  📂 **DB 관리**     : SQLite + SQLAlchemy 
  🖥️ **프론트엔드**   : HTML, CSS, Bootstrap
  🛠️ **백엔드**       : Flask (Python) 
 ────────────────────────────────────────────────────────

## 🏗️ 주요 기능

### ✅ 기본 기능

- **사용자 인증** (회원가입, 로그인, 로그아웃)
- **할 일 추가/수정/삭제**
- **할 일 완료 체크** (체크박스를 이용해 상태 변경)
- **마감 기일 설정**
- **우선순위 지정** (매우 낮음 \~ 매우 높음, 라디오 버튼 방식)
- **할 일 상세 보기** (할 일 제목 클릭 시 상세 페이지 이동)
- **로그인한 사용자별 할 일 관리** (자신의 할 일만 조회 가능)

### 🎨 UI 개선

- **마감 기일이 오늘이면 반짝이는 효과 적용** (CSS `@keyframes blink` 활용)
- **완료된 할 일은 반짝이지 않도록 조정**
- **할 일 목록을 마감 기일 순으로 정렬**
- **버튼 균형 조정** (`.task-buttons-detail` 개선)
- **삭제 버튼이 기존 폼 스타일 영향을 받지 않도록 조정** (`.task-detail-form` 추가)

---

## 🛠️ 기술 스택

### 📌 Backend

- Python, Flask
- Flask-SQLAlchemy (ORM 활용)
- Flask-WTF (Form 처리)
- Flask-Login (사용자 인증)
- SQLite (Database)

### 🎨 Frontend

- HTML, CSS (Bootstrap 사용 X)
- JavaScript (AJAX 요청을 이용한 상태 업데이트)

---

## 📂 프로젝트 구조

```
📁 프로젝트 루트
│── app.py               # Flask 애플리케이션 실행 파일
│── config.py            # 설정 파일
│── requirements.txt     # 필요한 라이브러리 목록
│── README.md            # 프로젝트 설명 파일
│
├─── models              # 데이터베이스 모델
│    ├── __init__.py      # DB 초기화
│    ├── user_model.py    # 사용자 모델
│    ├── task_model.py    # 할 일 모델
│
├─── forms               # Flask-WTF 폼 정의
│    ├── auth_form.py     # 로그인, 회원가입 폼
│    ├── task_form.py     # 할 일 추가/수정 폼
│
├─── routes              # Flask 라우트 관리
│    ├── auth_routes.py   # 사용자 인증 관련 라우트
│    ├── task_routes.py   # 할 일 관련 라우트
│
├─── templates           # HTML 템플릿
│    ├── base.html        # 기본 레이아웃
│    ├── login.html       # 로그인 페이지
│    ├── register.html    # 회원가입 페이지
│    ├── tasks.html       # 할 일 목록 페이지
│    ├── task_detail.html # 할 일 상세 페이지
│    ├── add_task.html    # 할 일 추가 페이지
│    ├── edit_task.html   # 할 일 수정 페이지
│
├─── static              # 정적 파일
│    ├── css
│    │   ├── styles.css   # 프로젝트 전체 스타일
```

---

## 🚀 실행 방법

### 1️⃣ 가상환경 설정 및 패키지 설치

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### 2️⃣ 데이터베이스 초기화

```bash
flask db init
flask db migrate -m "Initialize database"
flask db upgrade
```

### 3️⃣ Flask 애플리케이션 실행

```bash
flask run
```

---

## 🎯 향후 개선 계획

- **할 일 검색 및 필터 기능 추가**
- **Django 기반 API 서버로 확장 가능성 검토**
- **배포 환경 설정 (Heroku or Render)**

---

## 📜 개발자

- ** JELKOV
- ** [Github](https://github.com/JELKOV)

