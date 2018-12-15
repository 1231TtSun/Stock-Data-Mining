from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(255))
    password = db.Column(db.String(255))
    # @property
    # def password(self):
    #     raise AttributeError('password is not a readable attribute')
    # @password.setter
    # def password(self, password):
    #     # self.password = generate_password_hash(password)
    #     self.password=password
    # def verify_password(self, password):
    #     # return check_password_hash(self.password, password)
    #     if self.password==password:
    #         return True
    #     else:
    #         return False


class DB_ENV(db.Model):
    __tablename__ = 'db_env'
    key = db.Column(db.String(255), primary_key=True)
    value = db.Column(db.String(255))


class DB_LOG(db.Model):
    __tablename__ = 'db_log'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    commit_time = db.Column(db.String(255))
    start_time = db.Column(db.String(255))
    finish_time = db.Column(db.String(255))
    status = db.Column(db.String(255))
    error = db.Column(db.String(255))
    admin_id = db.Column(db.String(255))


class DB_TABLES(db.Model):
    __tablename__ = 'db_tables'
    table_name = db.Column(db.String(255), primary_key=True)
    description = db.Column(db.Text)
    update_time = db.Column(db.String(255))


class Stock_Basic(db.Model):
    __tablename__ = 'stock_basic'
    index = db.Column(db.BigInteger, primary_key=True)
    ts_code = db.Column(db.String(255))
    symbol = db.Column(db.Text)
    name = db.Column(db.Text)
    area = db.Column(db.Text)
    industry = db.Column(db.Text)
    fullname = db.Column(db.Text)
    enname = db.Column(db.Text)
    market = db.Column(db.Text)
    exchange = db.Column(db.Text)
    curr_type = db.Column(db.Text)
    list_status = db.Column(db.Text)
    list_date = db.Column(db.Text)
    delist_date = db.Column(db.Text)
    is_hs = db.Column(db.Text)


class Stock_Daily_Bar(db.Model):
    __tablename__ = 'stock_daily_bar'
    trade_date = db.Column(db.String(255), primary_key=True)
    ts_code = db.Column(db.String(255), primary_key=True)
    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    close = db.Column(db.Float)
    pre_close = db.Column(db.Float)
    change = db.Column(db.Float)
    pct_change = db.Column(db.Float)
    vol = db.Column(db.Float)
    amount = db.Column(db.Float)


class Model_TrendForecast(db.Model):
    __tablename__ = 'model_trendforecast'
    ts_code = db.Column(db.String(255), primary_key=True)
    pt = db.Column(db.String(255), primary_key=True)
    parameters = db.Column(db.BLOB)
    similar_stocks = db.Column(db.BLOB)
    expected_return = db.Column(db.BLOB)
    votes = db.Column(db.BLOB)


class Model_SimilarityShortTerm(db.Model):
    __tablename__ = 'model_similarityshortterm'
    ts_code = db.Column(db.String(255), primary_key=True)
    pt = db.Column(db.String(255), primary_key=True)
    parameters = db.Column(db.BLOB)
    similar_stocks = db.Column(db.BLOB)
    trendline = db.Column(db.BLOB)


class Model_SimilarHistory(db.Model):
    __tablename__ = 'model_similarhistory'
    ts_code = db.Column(db.String(255), primary_key=True)
    pt = db.Column(db.String(255), primary_key=True)
    parameters = db.Column(db.BLOB)
    similarduration = db.Column(db.BLOB)
    trendline = db.Column(db.BLOB)


class Model_StockActivity(db.Model):
    __tablename__ = 'model_stockactivity'
    ts_code = db.Column(db.String(255), primary_key=True)
    pt = db.Column(db.String(255), primary_key=True)
    parameters = db.Column(db.BLOB)
    similar_stocks = db.Column(db.BLOB)
    stockactivity = db.Column(db.BLOB)


class Model_SimilarTrend(db.Model):
    __tablename__ = 'model_similartrend'
    ts_code = db.Column(db.String(255), primary_key=True)
    pt = db.Column(db.String(255), primary_key=True)
    parameters = db.Column(db.BLOB)
    similar_stocks = db.Column(db.BLOB)
    activitybytrend = db.Column(db.BLOB)


class Model_CorrelationShortTerm(db.Model):
    __tablename__ = 'model_correlationshortterm'
    ts_code = db.Column(db.String(255), primary_key=True)
    pt = db.Column(db.String(255), primary_key=True)
    parameters = db.Column(db.BLOB)
    corr_stocks = db.Column(db.BLOB)
    trendline = db.Column(db.BLOB)


class Model_StateTransition(db.Model):
    __tablename__ = 'model_statetransition'
    ts_code = db.Column(db.String(255), primary_key=True)
    pt = db.Column(db.String(255), primary_key=True)
    s_up = db.Column(db.Float)
    s_blc = db.Column(db.Float)
    s_down = db.Column(db.Float)
    l_up = db.Column(db.Float)
    l_blc = db.Column(db.Float)
    l_down = db.Column(db.Float)
    parameters = db.Column(db.BLOB)


class Model_AssociateRule(db.Model):
    __tablename__ = 'model_ associaterule'
    ts_code_x = db.Column(db.String(255), primary_key=True)
    ts_code_y = db.Column(db.String(255))
    pt = db.Column(db.String(255), primary_key=True)
    up_rate = db.Column(db.Float)
    bic_rate = db.Column(db.Float)
    down_rate = db.Column(db.Float)
    parameters = db.Column(db.BLOB)


class Model_AmplitudePortfolio(db.Model):
    __tablename__ = ' model_amplitudeportfolio'
    ts_code = db.Column(db.String(255), primary_key=True)
    pt = db.Column(db.String(255), primary_key=True)
    index = db.Column(db.String(255))
    parameters = db.Column(db.BLOB)
    group_rate = db.Column(db.BLOB)


class Model_AmplitudeCorrelation(db.Model):
    __tablename__ = ' model_amplitudecorrelation'
    ts_code = db.Column(db.String(255), primary_key=True)
    pt = db.Column(db.String(255), primary_key=True)
    index = db.Column(db.String(255))
    support = db.Column(db.Float)
    parameters = db.Column(db.BLOB)
    group_rate = db.Column(db.BLOB)


class Model_AmplitudeStatistic(db.Model):
    __tablename__ = ' model_amplitudestatistic'
    ts_code = db.Column(db.String(255), primary_key=True)
    pt = db.Column(db.String(255), primary_key=True)
    close = db.Column(db.Float)
    down_rate = db.Column(db.Float)
    down_rank = db.Column(db.Float)
    up_rate = db.Column(db.Float)
    up_rank = db.Column(db.Float)
    all_rank = db.Column(db.Float)
    parameters = db.Column(db.BLOB)



