from . import main
from .form import LoginForm
from webapp.models import User
from flask import render_template,redirect,url_for
from flask_login import login_fresh,current_user,login_required,login_user

@main.route('login',methods=['GET'])
def login():
    if current_user is not None and current_user.is_authenticated:
        user = User.query.filter_by(nickname=current_user.nickname).first()
        login_user(user, True, None, False, False)
        return redirect(url_for('main.index'))
    form = LoginForm()
    return render_template('main/login.html', form=form)

@main.route('register',methods=['GET'])
def register():
    return 0

# @main.route('logout',methods=['GET'])
# @login_required
# def logout():
#     logout_user()
#     return 0

@main.route('index',methods=['GET'])
@login_required
def index():
    print(current_user)
    return render_template('main/index.html',fresh=login_fresh())

@main.route('database',methods=['GET'])
def database():
    return render_template('main/database.html')