from . import main
from webapp.models import User
from flask import render_template,redirect,url_for,session
from flask_login import login_fresh,current_user,login_required,login_user,logout_user

@main.route('login',methods=['GET'])
def login():
    if current_user is not None and current_user.is_authenticated:
        session['_fresh'] = False
        user = User.query.filter_by(id=current_user.id).first()
        login_user(user, True, None, False, False)
        return redirect(url_for('main.index'))
    return render_template('main/login.html')

@main.route('register',methods=['GET'])
def register():
    return render_template('main/register.html')

@main.route('logout',methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@main.route('recoverpassword',methods=['GET'])
def recoverpassword():
    return render_template('main/recoverpassword.html')

@main.route('lockscreen',methods=['GET'])
def lockscreen():
    return render_template('main/lockscreen.html')

@main.route('',methods=['GET'])
# @login_required
def index():
    return render_template('main/index.html',fresh=login_fresh())
    # return redirect(url_for())

@main.route('database',methods=['GET'])
def database():
    return render_template('main/database.html')

@main.route('test',methods=['GET'])
def test():
    return render_template('stock_base.html')

@main.route('zjlxqj',methods=['GET'])
def zjlxqj():
    return render_template('main/bkqj/cndtqj_zjlxqj.html')

@main.route('jyhyqj',methods=['GET'])
def jyhyqj():
    return render_template('main/bkqj/cndtqj_jyhyqj.html')

@main.route('zsbhqj',methods=['GET'])
def zsbhqj():
    return render_template('main/bkqj/cndtqj_zsbhqj.html')

@main.route('szfbqj',methods=['GET'])
def szfbqj():
    return render_template('main/bkqj/cndtqj_szfbqj.html')

@main.route('dtgzqj',methods=['GET'])
def dtgzqj():
    return render_template('main/bkqj/cndtqj_dtgzqj.html')

@main.route('djrdqj',methods=['GET'])
def djrdqj():
    return render_template('main/bkqj/cwdtqj_djrdqj.html')

@main.route('gbrqqj',methods=['GET'])
def gbrqqj():
    return render_template('main/bkqj/cwdtqj_gbrqqj.html')

@main.route('cwzbbj',methods=['GET'])
def cwzbbj():
    return render_template('main/bkqj/cwzbbj.html')

@main.route('hqsjbj',methods=['GET'])
def hqsjbj():
    return render_template('main/bkqj/hqsjbj.html')