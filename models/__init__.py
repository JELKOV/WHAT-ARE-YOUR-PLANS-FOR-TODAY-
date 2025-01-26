from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy 객체 초기화
todo_db = SQLAlchemy()

# 모델 가져오기
from .task_model import Task

