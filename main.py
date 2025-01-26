import os
from flask import Flask, render_template
from models import todo_db
from routes.task_routes import task_bp

def create_app():
    """
    Flask 애플리케이션을 생성 및 초기화하는 함수.
    데이터베이스를 초기화하고, 필요한 블루프린트를 등록합니다.
    """
    # Flask 애플리케이션 객체 생성
    app = Flask(__name__)
    # config.py 파일의 Config 클래스를 로드하여 설정 적용
    app.config.from_object('config.Config')

    # SQLAlchemy 초기화: 데이터베이스와 Flask 애플리케이션을 연결
    todo_db.init_app(app)

    # 작업(Task) 관련 라우트를 블루프린트로 등록
    app.register_blueprint(task_bp, url_prefix='/tasks')

    @app.route('/')
    def home():
        return render_template('home.html')

    return app

if __name__ == '__main__':
    app = create_app()

    # instance 디렉토리 확인 및 생성: 데이터베이스 파일이 저장될 디렉토리
    if not os.path.exists('instance'):
        os.makedirs('instance', exist_ok=True)

    # 데이터베이스 파일 확인: 존재하지 않을 경우 새로 생성
    db_path = os.path.join('instance', 'app.db')
    if not os.path.exists(db_path):
        with app.app_context():
            print("데이터 베이스 테이블 생성중...")
            # 데이터베이스 테이블 생성
            todo_db.create_all()
            print("데이터 베이스 테이블 생성완료.")

    # Flask 개발 서버 실행
    app.run(debug=True)
