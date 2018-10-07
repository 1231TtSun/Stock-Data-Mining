from . import main
from .form import LoginForm
from webapp.models import User
from flask import redirect,request,url_for
from flask_login import login_user

@main.route('api_login',methods=['POST'])
def api_login():
    form=LoginForm()
    if form.validate_on_submit():
        print(form.nickname.data)
        print(form.password.data)
        user = User.query.filter_by(nickname=form.nickname.data, password=form.password.data).first()
        if (user is not None):
            login_user(user, form.remember_me.data)
            # 此处应有next二次验证 避免重定向攻击
            return redirect(request.args.get("next") or url_for('main.index'))
        else:
            print("不存在的用户")
    else:
        return "1"

    # if current_user is not None and current_user.is_authenticated:
    #     # session['_fresh'] = False
    #     login_user(load_user(current_user.id), True, False, False)
    #     return redirect(url_for('index'))
    #     form = LoginForm()
    #     if form.validate_on_submit():
    #         user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    #         if (user is not None):
    #             login_user(user, form.remember_me.data)
    #             return redirect(request.args.get("next") or url_for('index'))
    #         else:
    #             print(form.errors)
    #     return 0




