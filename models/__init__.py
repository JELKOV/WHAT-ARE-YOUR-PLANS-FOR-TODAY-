# models/__init__.py
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy 객체 생성
todo_db = SQLAlchemy()

# 모델 등록
from .task_model import Task  # Task 모델
from .user_model import User  # User 모델
