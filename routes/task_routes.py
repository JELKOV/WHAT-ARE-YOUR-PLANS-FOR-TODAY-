from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from models import todo_db, Task
from forms.task_form import TaskForm
from datetime import datetime
from flask_login import login_required, current_user

# Blueprint 생성: 작업(Task) 관련 라우트를 관리하는 블루프린트
task_bp = Blueprint('tasks', __name__)

# 작업 목록을 조회하는 라우트
@task_bp.route('/')
@login_required  # ✅ 로그인한 사용자만 접근 가능
def task_list():
    """
    데이터베이스에서 모든 작업(Task)을 조회하여 렌더링합니다.
    """
    tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.deadline.asc()).all()
    today = datetime.today() # 오늘 날짜 가져오기
    weekday = today.strftime('%A')  #요일 가져오기
    return render_template('tasks.html', tasks=tasks, current_date=today.strftime("%Y-%m-%d"), weekday=weekday)# tasks.html 템플릿에 작업 데이터 전달

# 작업을 추가하는 라우트
@task_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_task():
    """
    새로운 작업(Task)을 추가하는 폼을 처리합니다.
    GET: 빈 폼을 렌더링.
    POST: 폼 데이터를 처리하여 데이터베이스에 작업을 추가.
    """
    form = TaskForm()  # 작업 추가를 위한 Flask-WTF 폼 생성
    if form.validate_on_submit():  # 폼 데이터가 유효한 경우
        new_task = Task(
            title=form.title.data,          # 제목 필드 값
            description=form.description.data,  # 설명 필드 값
            category=form.category.data,    # 카테고리 필드 값
            priority=form.priority.data,    # 우선순위 필드 값
            deadline=form.deadline.data,     # 마감일 필드 값
            user_id = current_user.id  # ✅ 현재 로그인한 사용자의 ID 저장
        )
        todo_db.session.add(new_task)  # 새로운 작업을 데이터베이스 세션에 추가
        todo_db.session.commit()       # 데이터베이스에 변경 사항 저장
        return redirect(url_for('tasks.task_list'))  # 작업 목록 페이지로 리다이렉트
    return render_template('add_task.html', form=form)  # add_task.html 템플릿 렌더링

# 작업을 수정하는 라우트
@task_bp.route('/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    """
    기존 작업(Task)을 수정하는 폼을 처리합니다.
    GET: 작업 데이터를 기반으로 채워진 폼을 렌더링.
    POST: 수정된 데이터를 처리하여 데이터베이스를 업데이트.
    """
    # 작업 ID로 작업을 조회. 없으면 404 에러 반환
    task = Task.query.get_or_404(task_id)

    # ✅ 현재 로그인한 사용자가 소유한 작업인지 확인
    if task.user_id != current_user.id:
        return "권한이 없습니다.", 403

    form = TaskForm(obj=task)  # 기존 작업 데이터를 기반으로 폼 생성
    if form.validate_on_submit():  # 폼 데이터가 유효한 경우
        task.title = form.title.data          # 제목 필드 업데이트
        task.description = form.description.data  # 설명 필드 업데이트
        task.category = form.category.data    # 카테고리 필드 업데이트
        task.priority = form.priority.data    # 우선순위 필드 업데이트
        task.deadline = form.deadline.data    # 마감일 필드 업데이트
        task.completed = form.completed.data  # ✅ 완료 여부 반영
        todo_db.session.commit()             # 데이터베이스에 변경 사항 저장
        return redirect(url_for('tasks.task_list'))  # 작업 목록 페이지로 리다이렉트
    return render_template('edit_task.html', form=form, task=task)  # edit_task.html 템플릿 렌더링

# 작업을 삭제하는 라우트
@task_bp.route('/delete/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):

    task = Task.query.get_or_404(task_id) # 작업 ID로 작업을 조회 , 없으면 404 에러 반환
    # 현재 로그인한 사용자가 삭제 가능 여부 판단
    if task.user_id != current_user.id:
        return "권한이 없습니다.", 403

    todo_db.session.delete(task) # 선택된 작업을 삭제
    todo_db.session.commit()  # db에 변경사항 저장
    return redirect(url_for('tasks.task_list')) # 작업 목록 페이지로 리로드


# 작업 상태 업데이트 (완료 체크)
@task_bp.route('/update_status/<int:task_id>', methods=['POST'])
def update_task_status(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    task.completed = data.get('completed', False)
    todo_db.session.commit()

    return jsonify({"success": True})

# 작업 상세 라우트
@task_bp.route('/detail/<int:task_id>')
def task_detail(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template('task_detail.html', task=task)
