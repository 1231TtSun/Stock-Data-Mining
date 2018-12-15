import pandas as pd
from lib.independent_models import engine

class data_set(object):
    __ds__=None
    def __init__(self,start_date='20050101',end_date='20181111'):
        sql_cmd = "select * from stock_daily_bar where trade_date>='" + start_date + "' and trade_date<='" + end_date + "'"
        self.__ds__ = pd.read_sql(sql=sql_cmd, con=engine)
        self.__ds__.set_index('ts_code',drop=False,append=True,inplace=True)
    def get_daily_bar(self,ts_code,start_date='20050101',end_date='20181111'):
        return self.__ds__[(self.__ds__['ts_code']==ts_code)]

def get_daily_bar(ts_code,start_date='20050101',end_date='20181111'):
    sql_cmd = "select * from stock_daily_bar where ts_code='"+ts_code+"' and trade_date>='"+start_date+"' and trade_date<='"+end_date+"'"
    df = pd.read_sql(sql=sql_cmd, con=engine)
    return df

def stock_basic():
    sql_cmd = "select * from stock_basic"
    df = pd.read_sql(sql=sql_cmd, con=engine)
    return df

def get_similar_industry_stock(ts_code):
    sql_cmd ="select * from stock_basic where industry=(select industry from stock_basic where ts_code='"+ ts_code +"');"
    df = pd.read_sql(sql=sql_cmd, con=engine)
    return df
    