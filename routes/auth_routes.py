from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash
from models import todo_db
from models.user_model import User
from forms.auth_form import LoginForm, RegisterForm

auth_bp = Blueprint('auth', __name__)

# Flask-Login 초기화
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('로그인 성공!', 'success')
            return redirect(url_for('home'))
        else:
            flash('사용자명 또는 비밀번호가 잘못되었습니다.', 'danger')
    return render_template('login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash('이미 존재하는 사용자명입니다.', 'danger')
            return redirect(url_for('auth.register'))
        user = User(
            username=form.username.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        todo_db.session.add(user)
        todo_db.session.commit()
        flash('회원가입 성공! 로그인해주세요.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('로그아웃되었습니다.', 'success')
    return redirect(url_for('auth.login'))
