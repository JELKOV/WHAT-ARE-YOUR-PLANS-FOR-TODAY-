import os
import dotenv

# .env 파일 로드: 환경 변수 값을 불러옵니다.
dotenv.load_dotenv()

# 프로젝트의 루트 디렉터리 경로 확인
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
print("BASE_DIR:", BASE_DIR)
print("DATABASE URI:", f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'app.db')}")

class Config:
    """
    Flask 애플리케이션의 설정 값을 정의하는 클래스.
    """
    # CSRF 보호 및 기타 보안 기능에 필요한 비밀 키 설정
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')
    # SQLite 데이터베이스 경로 설정
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'app.db')}"
    # SQLAlchemy 경고 비활성화: 성능 최적화를 위해 변경 사항 추적 기능을 비활성화
    SQLALCHEMY_TRACK_MODIFICATIONS = False
