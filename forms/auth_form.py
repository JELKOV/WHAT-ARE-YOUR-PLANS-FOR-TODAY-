from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField('사용자명', validators=[
        DataRequired(message="사용자명을 입력해주세요."),
        Length(min=3, max=20, message="사용자명은 3자에서 20자 사이여야 합니다.")
    ])
    password = PasswordField('비밀번호', validators=[
        DataRequired(message="비밀번호를 입력해주세요.")
    ])
    submit = SubmitField('로그인')

class RegisterForm(FlaskForm):
    username = StringField('사용자명', validators=[
        DataRequired(message="사용자명을 입력해주세요."),
        Length(min=3, max=20, message="사용자명은 3자에서 20자 사이여야 합니다.")
    ])
    email = StringField('이메일', validators=[
        DataRequired(message="이메일을 입력해주세요."),
        Email(message="올바른 이메일 형식이 아닙니다.")
    ])
    password = PasswordField('비밀번호', validators=[
        DataRequired(message="비밀번호를 입력해주세요."),
        Length(min=6, message="비밀번호는 최소 6자 이상이어야 합니다.")
    ])
    confirm_password = PasswordField('비밀번호 확인', validators=[
        DataRequired(message="비밀번호 확인을 입력해주세요."),
        EqualTo('password', message="비밀번호가 일치하지 않습니다.")
    ])
    submit = SubmitField('회원가입')
