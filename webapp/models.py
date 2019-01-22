from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    emailaddress=db.Column(db.String(255))
    username = db.Column(db.String(255))
    password_hash=db.Column(db.String(255))
    avatar=db.Column(db.String(255))
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class gpgz_hypjsyl(db.Model):
    riqi=db.Column(db.String(255))
    gupiao=db.Column(db.String(255))
    gupiaope=db.Column(db.String(255))
    zhengjianhuipe=db.Column(db.String(255))
    guozhengpe=db.Column(db.String(255))

class gpgz_lsxssy(db.Model):
    riqi=db.Column(db.String(255))
    gupiao=db.Column(db.String(255))
    gujia=db.Column(db.String(255))
    guzhi=db.Column(db.String(255))
    68shang=db.Column(db.String(255))
    68xia=db.Column(db.String(255))
    95shang=db.Column(db.String(255))
    95xia=db.Column(db.String(255))
    99shang=db.Column(db.String(255))
    99xia=db.Column(db.String(255))

class gpwj_bsd(db.Model):
    riqi=db.Column(db.String(255))
    gupiao=db.Column(db.String(255))
    buydian=db.Column(db.String(255))
    selldian=db.Column(db.String(255))
    fangshi=db.Column(db.String(255))

class gpwj_cqqr(db.Model):
    riqi=db.Column(db.String(255))
    gupiao=db.Column(db.String(255))
    xiadie=db.Column(db.String(255))
    chiping=db.Column(db.String(255))
    shangzhang=db.Column(db.String(255))
    fangshi=db.Column(db.String(255))

class gpwj_dqxg(db.Model):
    riqi=db.Column(db.String(255))
    gupiao=db.Column(db.String(255))
    xiangguan=db.Column(db.String(255))

class gpwj_dqxs(db.Model):
    riqi=db.Column(db.String(255))
    gupiao=db.Column(db.String(255))
    xiangsi=db.Column(db.String(255))

class gpwj_jqzd(db.Model):
    riqi=db.Column(db.String(255))
    gupiao=db.Column(db.String(255))
    qushi=db.Column(db.String(255))
    qushitoupiao=db.Column(db.String(255))
    xiangsigupiao=db.Column(db.String(255))

class gpwj_ldzd(db.Model):
    riqi=db.Column(db.String(255))
    gupiao=db.Column(db.String(255))
    guize=db.Column(db.String(255))

class gpwj_tzdgp(db.Model):
    riqi=db.Column(db.String(255))
    gupiao=db.Column(db.String(255))
    gupiaoliebiao=db.Column(db.String(255))
    huoyueduliebiao=db.Column(db.String(255))

class gpwj_tzsgp(db.Model):
    riqi=db.Column(db.String(255))
    gupiao=db.Column(db.String(255))
    gupiaoliebiao=db.Column(db.String(255))
    huoyueduliebiao=db.Column(db.String(255))

class gpwj_zdfpx(db.Model):
    riqi=db.Column(db.String(255))
    gupiao=db.Column(db.String(255))
    shoupanjia=db.Column(db.String(255))
    xiangduigaodian=db.Column(db.String(255))
    diefupaixu=db.Column(db.String(255))
    xiangduididian=db.Column(db.String(255))
    zhangfupaixu=db.Column(db.String(255))
    tubiao=db.Column(db.String(255))

class gpwj_zsli(db.Model):
    riqi=db.Column(db.String(255))
    gupiao=db.Column(db.String(255))
    lishi=db.Column(db.String(255))


class guwj_fzzhgl(db.Model):
    riqi=db.Column(db.String(255))
    gupiao=db.Column(db.String(255))
    qianjianshu=db.Column(db.String(255))
    qianjian=db.Column(db.String(255))
    houjian=db.Column(db.String(255))
    zhichidu=db.Column(db.String(255))
    zhixindu=db.Column(db.String(255))
    fenzifenmu=db.Column(db.String(255))

class guwj_fzzhtj(db.Model):
    riqi=db.Column(db.String(255))
    gupiao=db.Column(db.String(255))
    yuanci=db.Column(db.String(255))
    d4=db.Column(db.String(255))
    d3=db.Column(db.String(255))
    d2=db.Column(db.String(255))
    d1=db.Column(db.String(255))
    d0=db.Column(db.String(255))
    zongcishu=db.Column(db.String(255))
    chuxiancishu=db.Column(db.String(255))
    cishuzhanbi=db.Column(db.String(255))





















