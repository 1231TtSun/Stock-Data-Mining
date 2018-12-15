from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
engine=create_engine('mysql+pymysql://root:0000@116.196.90.212:3306/finmagic?charset=utf8')
Base = declarative_base()
Session = sessionmaker(bind=engine)
class Stock_Daily_Bar(Base):
    __tablename__ = 'stock_daily_bar'
    trade_date = db.Column(db.String(255),primary_key=True)
    ts_code=db.Column(db.String(255),primary_key=True)
    open=db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    close = db.Column(db.Float)
    pre_close = db.Column(db.Float)
    change = db.Column(db.Float)
    pct_change = db.Column(db.Float)
    vol = db.Column(db.Float)
    amount = db.Column(db.Float)