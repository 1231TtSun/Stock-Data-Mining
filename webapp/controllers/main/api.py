from . import main
from webapp.models import db,User
from flask import redirect,request,url_for
from flask_login import login_user,current_user

@main.route('api_login',methods=['POST'])
def api_login():
    emailaddress=request.form.get('emailaddress')
    password=request.form.get('password')
    user = User.query.filter_by(emailaddress=emailaddress).first()
    if (user is not None):
        if(user.verify_password(password)):
            login_user(user,request.form.get("remember"))
            # 此处应有next二次验证 避免重定向攻击
            return redirect(request.args.get("next") or url_for('main.index'))
        else:
            print("密码错误")
    else:
        print("不存在的用户")

@main.route('api_register',methods=['POST'])
def api_register():
    username=request.form.get('username')
    emailaddress=request.form.get('emailaddress')
    password=request.form.get('password')
    confirmpassword=request.form.get('confirmpassword')
    if(User.query.filter_by(emailaddress=emailaddress).first() is not None):
        print("该邮箱已被使用")
    elif(password!=confirmpassword):
        print("密码不一致")
    else:
        new_user=User()
        new_user.username=username
        new_user.emailaddress=emailaddress
        new_user.password=password
        db.session.add(new_user)
        db.session.commit()

@main.route('api_lockscreen',methods=['POST'])
def api_lockscreen():
    password=request.form.get("password")
    if current_user is not None and current_user.is_authenticated:
        user = User.query.filter_by(id=current_user.id).first()
        if(user.verify_password(password)):
            login_user(user,True)
            return redirect(request.args.get("next") or url_for('main.index'))
        else:
            print("密码错误")
    else:
        return redirect(url_for("main.index"))




