from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from models import todo_db

class User(todo_db.Model, UserMixin):
    """
    사용자 모델 클래스. Flask-Login의 UserMixin을 사용해 인증 기능 추가.
    """
    __tablename__ = 'users'
    id = todo_db.Column(todo_db.Integer, primary_key=True)
    username = todo_db.Column(todo_db.String(80), unique=True, nullable=False)
    email = todo_db.Column(todo_db.String(120), unique=True, nullable=False)
    password_hash = todo_db.Column(todo_db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'
