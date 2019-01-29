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


# class gpgz_hypjsyl(db.Model):
#     riqi=db.Column(db.String(255))
#     gupiao=db.Column(db.String(255))
#     gupiaope=db.Column(db.String(255))
#     zhengjianhuipe=db.Column(db.String(255))
#     guozhengpe=db.Column(db.String(255))

# class gpgz_lsxssy(db.Model):
#     riqi=db.Column(db.String(255))
#     gupiao=db.Column(db.String(255))
#     gujia=db.Column(db.String(255))
#     guzhi=db.Column(db.String(255))
#     68shang=db.Column(db.String(255))
#     68xia=db.Column(db.String(255))
#     95shang=db.Column(db.String(255))
#     95xia=db.Column(db.String(255))
#     99shang=db.Column(db.String(255))
#     99xia=db.Column(db.String(255))

# class gpwj_bsd(db.Model):
#     riqi=db.Column(db.String(255))
#     gupiao=db.Column(db.String(255))
#     buydian=db.Column(db.String(255))
#     selldian=db.Column(db.String(255))
#     fangshi=db.Column(db.String(255))
#
# class gpwj_cqqr(db.Model):
#     riqi=db.Column(db.String(255))
#     gupiao=db.Column(db.String(255))
#     xiadie=db.Column(db.String(255))
#     chiping=db.Column(db.String(255))
#     shangzhang=db.Column(db.String(255))
#     fangshi=db.Column(db.String(255))
#
# class gpwj_dqxg(db.Model):
#     riqi=db.Column(db.String(255))
#     gupiao=db.Column(db.String(255))
#     xiangguan=db.Column(db.String(255))
#
# class gpwj_dqxs(db.Model):
#     riqi=db.Column(db.String(255))
#     gupiao=db.Column(db.String(255))
#     xiangsi=db.Column(db.String(255))
#
# class gpwj_jqzd(db.Model):
#     riqi=db.Column(db.String(255))
#     gupiao=db.Column(db.String(255))
#     qushi=db.Column(db.String(255))
#     qushitoupiao=db.Column(db.String(255))
#     xiangsigupiao=db.Column(db.String(255))
#
# class gpwj_ldzd(db.Model):
#     riqi=db.Column(db.String(255))
#     gupiao=db.Column(db.String(255))
#     guize=db.Column(db.String(255))
#
# class gpwj_tzdgp(db.Model):
#     riqi=db.Column(db.String(255))
#     gupiao=db.Column(db.String(255))
#     gupiaoliebiao=db.Column(db.String(255))
#     huoyueduliebiao=db.Column(db.String(255))
#
# class gpwj_tzsgp(db.Model):
#     riqi=db.Column(db.String(255))
#     gupiao=db.Column(db.String(255))
#     gupiaoliebiao=db.Column(db.String(255))
#     huoyueduliebiao=db.Column(db.String(255))
#
# class gpwj_zdfpx(db.Model):
#     riqi=db.Column(db.String(255))
#     gupiao=db.Column(db.String(255))
#     shoupanjia=db.Column(db.String(255))
#     xiangduigaodian=db.Column(db.String(255))
#     diefupaixu=db.Column(db.String(255))
#     xiangduididian=db.Column(db.String(255))
#     zhangfupaixu=db.Column(db.String(255))
#     tubiao=db.Column(db.String(255))
#
# class gpwj_zsli(db.Model):
#     riqi=db.Column(db.String(255))
#     gupiao=db.Column(db.String(255))
#     lishi=db.Column(db.String(255))
#
#
# class guwj_fzzhgl(db.Model):
#     riqi=db.Column(db.String(255))
#     gupiao=db.Column(db.String(255))
#     qianjianshu=db.Column(db.String(255))
#     qianjian=db.Column(db.String(255))
#     houjian=db.Column(db.String(255))
#     zhichidu=db.Column(db.String(255))
#     zhixindu=db.Column(db.String(255))
#     fenzifenmu=db.Column(db.String(255))
#
# class guwj_fzzhtj(db.Model):
#     riqi=db.Column(db.String(255))
#     gupiao=db.Column(db.String(255))
#     yuanci=db.Column(db.String(255))
#     d4=db.Column(db.String(255))
#     d3=db.Column(db.String(255))
#     d2=db.Column(db.String(255))
#     d1=db.Column(db.String(255))
#     d0=db.Column(db.String(255))
#     zongcishu=db.Column(db.String(255))
#     chuxiancishu=db.Column(db.String(255))
#     cishuzhanbi=db.Column(db.String(255))

class jccwsj(db.Model):
    __tablename__ = 'jccwsj'
    id = db.Column(db.Integer)
    ts_code=db.Column(db.String(255),primary_key=True)
    sec_name=db.Column(db.String(255))
    date=db.Column(db.String(255),primary_key=True)
    eps_basic_is=db.Column(db.Float)
    net_cash_flows_oper_act=db.Column(db.Float)
    tot_cur_assets=db.Column(db.Float)
    tot_cur_liab=db.Column(db.Float)
    tot_profit=db.Column(db.Float)
    tot_liab=db.Column(db.Float)
    net_profit_is=db.Column(db.Float)
    oper_profit=db.Column(db.Float)
    net_incr_cash_cash_equ_dm=db.Column(db.Float)
    net_invest_inc=db.Column(db.Float)
    tot_assets=db.Column(db.Float)
    oper_cost=db.Column(db.Float)
    monetary_cap=db.Column(db.Float)
    long_term_rec=db.Column(db.Float)
    tot_non_cur_liab=db.Column(db.Float)
    inventories=db.Column(db.Float)
    cash_cash_equ_beg_period=db.Column(db.Float)
    cash_cash_equ_end_period=db.Column(db.Float)
    net_cash_flows_fnc_act=db.Column(db.Float)
    net_cash_flows_inv_act=db.Column(db.Float)
    selling_dist_exp=db.Column(db.Float)
    gerl_admin_exp=db.Column(db.Float)
    fin_exp_is=db.Column(db.Float)
    taxes_surcharges_ops=db.Column(db.Float)
    cap_stk=db.Column(db.Float)
    oper_rev=db.Column(db.Float)
    net_fixed_assets=db.Column(db.Float)
    net_non_oper_income=db.Column(db.Float)
    net_asset_per=db.Column(db.Float)
    net_cash_flows_oper_act_per=db.Column(db.Float)
    main_oper_rev=db.Column(db.Float)
    main_oper_profit=db.Column(db.Float)
    main_oper_cost=db.Column(db.Float)
    main_oper_tax=db.Column(db.Float)
    net_profit_is_excluded=db.Column(db.Float)
    tot_equity=db.Column(db.Float)
    income_tax_expenses=db.Column(db.Float)
    eps_diluted_is=db.Column(db.Float)
    tot_cost=db.Column(db.Float)
    ave_assets_oper_income=db.Column(db.Float)
    sale_rev=db.Column(db.Float)
    ave_net_assets=db.Column(db.Float)
    tax_cost=db.Column(db.Float)
    non_main_oper_rec=db.Column(db.Float)
    long_term_debt=db.Column(db.Float)
    long_assets=db.Column(db.Float)
    long_capital=db.Column(db.Float)
    working_capital=db.Column(db.Float)
    intang_assets=db.Column(db.Float)
    sh_rights=db.Column(db.Float)
    sale_cost=db.Column(db.Float)
    net_cash_flow=db.Column(db.Float)
    rate_rec_on_net_asset=db.Column(db.Float)
class jccwzb(db.Model):
    __tablename__ = 'jccwzb'
    id = db.Column(db.Integer)
    ts_code=db.Column(db.String(255),primary_key=True)
    sec_name=db.Column(db.String(255))
    date=db.Column(db.String(255),primary_key=True)
    rate_return_on_tot_asset=db.Column(db.Float)
    rate_return_on_cost=db.Column(db.Float)
    net_profit_margin=db.Column(db.Float)
    rate_return_on_net_asset=db.Column(db.Float)
    three_cost_proportion=db.Column(db.Float)
    pro_margin_main_business=db.Column(db.Float)
    oper_profit_margin=db.Column(db.Float)
    rate_return_on_equity=db.Column(db.Float)
    rate_return_on_asset=db.Column(db.Float)
    non_main_proportion=db.Column(db.Float)
    rate_net_return_on_tot_asset=db.Column(db.Float)
    cost_rate_main_business=db.Column(db.Float)
    rate_equity_reward=db.Column(db.Float)
    rate_gross_sales_interest=db.Column(db.Float)
    ratio_main_profit=db.Column(db.Float)
    ratio_current=db.Column(db.Float)
    ratio_long_debts_working_captial=db.Column(db.Float)
    ratio_long_assets_long_captial=db.Column(db.Float)
    ratio_liquidation_value=db.Column(db.Float)
    ratio_quick=db.Column(db.Float)
    ratio_sh_equity=db.Column(db.Float)
    ratio_capitalization=db.Column(db.Float)
    ratio_share_equity=db.Column(db.Float)
    ratio_cash=db.Column(db.Float)
    ratio_long_debt=db.Column(db.Float)
    ration_net_value_fixed_assets=db.Column(db.Float)
    ratio_interest_coverage=db.Column(db.Float)
    ration_sh_right_fixed_assets=db.Column(db.Float)
    ratio_capital_immobilization=db.Column(db.Float)
    ratio_asset_liability=db.Column(db.Float)
    ratio_debt_right=db.Column(db.Float)
    ratio_property_right=db.Column(db.Float)
    growth_rate_main_business_income=db.Column(db.Float)
    growth_rate_net_profit=db.Column(db.Float)
    growth_rate_net_assets=db.Column(db.Float)
    growth_rate_tot_assets=db.Column(db.Float)
    rate_receivable_turnover=db.Column(db.Float)
    days_inventory_turnover_oper_income=db.Column(db.Float)
    rate_assets_oper_cash_flow=db.Column(db.Float)
    days_receivable_turnover=db.Column(db.Float)
    days_tot_assets_turnover=db.Column(db.Float)
    ratio_oper_cash_net_profit=db.Column(db.Float)
    ratio_inventory_turnover=db.Column(db.Float)
    ratio_current_assets_turnover=db.Column(db.Float)
    ratio_oper_cash_debt=db.Column(db.Float)
    ratio_fixed_assets_turnover=db.Column(db.Float)
    days_current_assets_turnover=db.Column(db.Float)
    ratio_cash_flow=db.Column(db.Float)
    ratio_tot_assets_turnover=db.Column(db.Float)
    ratio_net_assets = db.Column(db.Float)
    ratio_fixed_assets = db.Column(db.Float)
    ratio_oper_cash_income=db.Column(db.Float)
class lrbzy(db.Model):
    __tablename__ = 'lrbzy'
    id = db.Column(db.Integer)
    index_cns_name=db.Column(db.String(255))
    index_eng_name=db.Column(db.String(255),primary_key=True)
    data_source=db.Column(db.String(255))
class zcfzbzy(db.Model):
    __tablename__ = 'zcfzbzy'
    id = db.Column(db.Integer)
    index_cns_name=db.Column(db.String(255))
    index_eng_name=db.Column(db.String(255),primary_key=True)
    data_source = db.Column(db.String(255))
class xjllbzy(db.Model):
    __tablename__ = 'xjllbzy'
    id = db.Column(db.Integer)
    index_cns_name=db.Column(db.String(255))
    index_eng_name=db.Column(db.String(255),primary_key=True)
    data_source = db.Column(db.String(255))
class cwbg(db.Model):
    __tablename__ = 'cwbg'
    id = db.Column(db.Integer)
    index_cns_name=db.Column(db.String(255))
    index_eng_name=db.Column(db.String(255),primary_key=True)
    data_source = db.Column(db.String(255))
class ylnl(db.Model):
    __tablename__ = 'ylnl'
    id = db.Column(db.Integer)
    index_cns_name=db.Column(db.String(255))
    index_eng_name=db.Column(db.String(255),primary_key=True)
    data_source = db.Column(db.String(255))
class chnl(db.Model):
    __tablename__ = 'chnl'
    id = db.Column(db.Integer)
    index_cns_name=db.Column(db.String(255))
    index_eng_name=db.Column(db.String(255),primary_key=True)
    data_source = db.Column(db.String(255))
class cznl(db.Model):
    __tablename__ = 'cznl'
    id = db.Column(db.Integer)
    index_cns_name=db.Column(db.String(255))
    index_eng_name=db.Column(db.String(255),primary_key=True)
    data_source = db.Column(db.String(255))
class yynl(db.Model):
    __tablename__ = 'yynl'
    id = db.Column(db.Integer)
    index_cns_name=db.Column(db.String(255))
    index_eng_name=db.Column(db.String(255),primary_key=True)
    data_source = db.Column(db.String(255))
class zycwzb(db.Model):
    __tablename__ = 'zycwzb'
    id = db.Column(db.Integer)
    index_cns_name=db.Column(db.String(255))
    index_eng_name=db.Column(db.String(255),primary_key=True)
    data_source = db.Column(db.String(255))
class jcsj_gsgk(db.Model):
    __tablename__ = 'jcsj_gsgk'
    id = db.Column(db.Integer)
    ts_code=db.Column(db.String(255),primary_key=True)
    full_name=db.Column(db.String(255))
    website=db.Column(db.String(255))
    eng_name=db.Column(db.String(255))
    short_name=db.Column(db.String(255))
    address=db.Column(db.String(255))
    legal_representative=db.Column(db.String(255))
    boardchairmen=db.Column(db.String(255))
    regist_captial=db.Column(db.String(255))
    industry=db.Column(db.String(255))
    phone=db.Column(db.String(255))
    fax=db.Column(db.String(255))
    raise_date=db.Column(db.String(255))
    exch_date=db.Column(db.String(255))
    pub_num=db.Column(db.Integer)
    pub_style=db.Column(db.String(255))
    pub_price=db.Column(db.Float)
    pub_ttm=db.Column(db.Float)
    main_underwriter=db.Column(db.String(255))
    to_underwriter=db.Column(db.String(255))
    exch_sponsors=db.Column(db.String(255))
    sponsor_agency=db.Column(db.String(255))
class jcsj_fxcz(db.Model):
    __tablename__ = 'jcsj_fxcz'
    id = db.Column(db.Integer)
    ts_code=db.Column(db.String(255),primary_key=True)
    pub_type=db.Column(db.String(255))
    pub_date=db.Column(db.String(255))
    pub_character=db.Column(db.String(255))
    pub_stock_type=db.Column(db.String(255))
    pub_style=db.Column(db.String(255))
    pub_stock_num=db.Column(db.Integer)
    pub_price_cns=db.Column(db.Float)
    pub_price_fore=db.Column(db.Float)
    act_fund=db.Column(db.Float)
    act_cost=db.Column(db.Float)
    pub_ttm=db.Column(db.Float)
    lot_rate_oniline_pricing=db.Column(db.Float)
    bid_rate_sec_distribution=db.Column(db.Float)
class jcsj_fxpg(db.Model):
    __tablename__ = 'jcsj_fxpg'
    id = db.Column(db.Integer)
    ts_code=db.Column(db.String(255),primary_key=True)
    bonus_year=db.Column(db.String(255))
    bonus_plan=db.Column(db.String(255))
    date_equity_regist=db.Column(db.String(255))
    date_exclusion=db.Column(db.String(255))
    date_bonus_shares=db.Column(db.String(255))
class jcsj_ggry(db.Model):
    __tablename__ = 'jcsj_ggry'
    id = db.Column(db.Integer)
    ts_code=db.Column(db.String(255),primary_key=True)
    name=db.Column(db.String(255),primary_key=True)
    birth_year=db.Column(db.String(255),primary_key=True)
    education=db.Column(db.String(255))
    sex=db.Column(db.String(255),primary_key=True)
    post=db.Column(db.String(255))
class jcsj_sdgd(db.Model):
    __tablename__ = 'jcsj_sdgd'
    id = db.Column(db.Integer)
    ts_code=db.Column(db.String(255),primary_key=True)
    date=db.Column(db.String(255),primary_key=True)
    name=db.Column(db.String(255),primary_key=True)
    num=db.Column(db.Float)
    ratio=db.Column(db.Float)
    type=db.Column(db.String(255))
class jcsj_ltgd(db.Model):
    __tablename__ = 'jcsj_ltgd'
    id = db.Column(db.Integer)
    ts_code=db.Column(db.String(255),primary_key=True)
    date=db.Column(db.String(255),primary_key=True)
    name=db.Column(db.String(255),primary_key=True)
    num = db.Column(db.Float)
    ratio = db.Column(db.Float)
    type=db.Column(db.String(255))
class jcsj_zczd(db.Model):
    __tablename__ = 'jcsj_zczd'
    id = db.Column(db.Integer)
    ts_code=db.Column(db.String(255),primary_key=True)
    type=db.Column(db.String(255))
    title=db.Column(db.String(255),primary_key=True)
class jcsj_gsgg(db.Model):
    __tablename__ = 'jcsj_gsgg'
    id = db.Column(db.Integer)
    ts_code=db.Column(db.String(255),primary_key=True)
    date=db.Column(db.String(255),primary_key=True)
    title=db.Column(db.String(255),primary_key=True)
    type=db.Column(db.String(255))
class jcsj_ggzx(db.Model):
    __tablename__ = 'jcsj_ggzx'
    id = db.Column(db.Integer)
    ts_code=db.Column(db.String(255),primary_key=True)
    date=db.Column(db.String(255),primary_key=True)
    title=db.Column(db.String(255),primary_key=True)
    time=db.Column(db.String(255))
class jcsj_hyzx(db.Model):
    __tablename__ = 'jcsj_hyzx'
    id = db.Column(db.Integer)
    ts_code=db.Column(db.String(255),primary_key=True)
    date=db.Column(db.String(255),primary_key=True)
    title=db.Column(db.String(255),primary_key=True)
    time=db.Column(db.String(255))
class jcsj_hdcf(db.Model):
    __tablename__ = 'jcsj_hdcf'
    id = db.Column(db.Integer)
    ts_code=db.Column(db.String(255),primary_key=True)
    date=db.Column(db.String(255),primary_key=True)
    title=db.Column(db.String(255),primary_key=True)
    type=db.Column(db.String(255))
class bkqj_cndtqj(db.Model):
    __tablename__ = 'bkqj_cndtqj'
    id = db.Column(db.Integer)
    industry_name=db.Column(db.String(255),primary_key=True)
    date=db.Column(db.String(255),primary_key=True)
    transaction_capital=db.Column(db.Float)
    ave_turnover_rate=db.Column(db.Float)
    ave_up_downs=db.Column(db.Float)
    cur_market_value=db.Column(db.Float)
    ave_ttm=db.Column(db.Float)
class bkqj_cwdtqj(db.Model):
    __tablename__ = 'bkqj_cwdtqj'
    id = db.Column(db.Integer)
    industry_name=db.Column(db.String(255),primary_key=True)
    date=db.Column(db.String(255),primary_key=True)
    all_click_num=db.Column(db.Integer)
    post_num=db.Column(db.Integer)
class bkqj_cwzbbj(db.Model):
    __tablename__ = 'bkqj_cwzbbj'
    id = db.Column(db.Integer)
    index_cns_name=db.Column(db.String(255))
    index_eng_name=db.Column(db.String(255),primary_key=True)
    data_source = db.Column(db.String(255))
class bkqj_hqsjbj(db.Model):
    __tablename__ = 'bkqj_hqsjbj'
    id = db.Column(db.Integer)
    index_cns_name=db.Column(db.String(255))
    index_eng_name=db.Column(db.String(255),primary_key=True)
    data_source = db.Column(db.String(255))
class jcrxsj(db.Model):
    __tablename__ = 'jcrxsj'
    id = db.Column(db.Integer)
    ts_code=db.Column(db.String(255),primary_key=True)
    ts_name=db.Column(db.String(255))
    trade_date=db.Column(db.String(255),primary_key=True)
    pct_change = db.Column(db.Float)
    current=db.Column(db.Float)
    open=db.Column(db.Float)
    high=db.Column(db.Float)
    low=db.Column(db.Float)
    pre_close=db.Column(db.Float)
    turnover_rate=db.Column(db.Float)
    vol=db.Column(db.Float)
    amount=db.Column(db.Float)
    cir_value=db.Column(db.Float)
    pe_ttm=db.Column(db.Float)
    pb=db.Column(db.Float)
    market_value=db.Column(db.Float)
    score=db.Column(db.Float)




















