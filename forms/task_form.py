from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, DateField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Optional

class TaskForm(FlaskForm):
    """
    작업(Task)을 추가 또는 수정하기 위한 Flask-WTF 기반의 폼.
    """
    # 제목 필드: 필수 입력 (제목은 빈 값일 수 없음)
    title = StringField('제목', validators=[DataRequired()])
    # 설명 필드: 선택 입력 (설명을 제공하지 않아도 됨)
    description = TextAreaField('설명', validators=[Optional()])
    # 카테고리 필드: 선택 입력 (카테고리를 지정하지 않아도 됨)
    category = StringField('카테고리', validators=[Optional()])
    # 우선순위 필드: 선택 입력 (숫자 입력, 기본값은 1)
    priority = IntegerField('우선순위(기본값은 1)', validators=[Optional()])
    # 마감일 필드: 선택 입력 (YYYY-MM-DD 형식의 날짜)
    deadline = DateField('마감기일', format='%Y-%m-%d', validators=[Optional()])
    # 완료 여부
    completed = BooleanField('완료 여부')  # ✅ 추가
    # 저장 버튼
    submit = SubmitField('저장 하기')
