# models/__init__.py에서 초기화된 SQLAlchemy 객체를 가져옴
from models import todo_db

class Task(todo_db.Model):
    """
    작업(Task) 정보를 저장하는 데이터베이스 모델.
    """
    # 데이터베이스에 생성될 테이블 이름
    __tablename__ = "tasks"
    # 기본 키: 고유 식별자
    id = todo_db.Column(todo_db.Integer, primary_key=True)
    # 작업 제목: 필수 입력 필드
    title = todo_db.Column(todo_db.String(100), nullable=False)
    # 작업 설명: 선택 입력 필드
    description = todo_db.Column(todo_db.Text, nullable=True)
    # 작업 카테고리: 선택 입력 필드
    category = todo_db.Column(todo_db.String(50), nullable=True)
    # 작업 우선순위: 기본값은 1
    priority = todo_db.Column(todo_db.Integer, default=1)
    # 작업 마감일: 선택 입력 필드
    deadline = todo_db.Column(todo_db.DateTime, nullable=True)
    # 작업 상태: 기본값은 'pending'
    status = todo_db.Column(todo_db.String(20), default='pending')
    # ✅ 완료 여부 추가
    completed = todo_db.Column(todo_db.Boolean, default=False)

    # 사용자 외래키 추가 (User 모델과 연결)
    user_id = todo_db.Column(todo_db.Integer, todo_db.ForeignKey('users.id'), nullable=False)

    # ✅ User 모델과 관계 설정 (각 Task는 하나의 User에 속함)
    user = todo_db.relationship('User', backref='tasks', lazy=True)

    def __repr__(self):
        return f'<Task {self.title} (User ID: {self.user_id})>'