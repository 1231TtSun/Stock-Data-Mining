from datetime import timedelta, datetime
import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean
from lib.fundamental_function import similarity_calculation
from lib import stock_database as sd


class TrendForecast(object):
    ts_code = None
    prediction_time_point = None
    matching_period = 30
    matching_range = 1
    __ob_window__ = 5
    __error__ = False
    __similar_stock__ = None
    __first_pct_change__ = None
    __second_pct_change__ = None
    __third_pct_change__ = None

    def __init__(self, ts_code, prediction_time_point, matching_period=30, matching_range=1):
        self.ts_code = ts_code
        self.prediction_time_point = prediction_time_point
        self.matching_period = matching_period
        self.matching_range = matching_range

    def __getx_data_start_time_point__(self):
        c_t = datetime.strptime(self.prediction_time_point, "%Y%m%d")
        s_t = c_t - timedelta(days=self.matching_period)
        return datetime.strftime(s_t, "%Y%m%d")

    def __gety_data_start_time_point__(self):
        c_t = datetime.strptime(self.prediction_time_point, "%Y%m%d")
        s_t = c_t.replace(year=c_t.year - self.matching_range)
        return datetime.strftime(s_t, "%Y%m%d")

    def __gety_data_end_time_point__(self):
        c_t = datetime.strptime(self.prediction_time_point, "%Y%m%d")
        e_t = c_t - timedelta(days=self.__ob_window__)
        return datetime.strftime(e_t, "%Y%m%d")

    # 取出除自己外最相似的十个股票时间段
    def __getSimilarStock__(self):
        result_dis = []
        result_dt = []
        result_ts = []
        stock_list = sd.get_similar_industry_stock(self.ts_code)
        x_data = sd.get_daily_bar(self.ts_code, self.__getx_data_start_time_point__(), self.prediction_time_point)
        if x_data.empty:
            self.__error__ = True
            return None
        else:
            x = np.array(x_data['pct_change'])
            ob_length = len(x)
            for index, row in stock_list.iterrows():
                stock = row['ts_code']
                if stock != self.ts_code:
                    y_data = sd.get_daily_bar(stock, self.__gety_data_start_time_point__(),
                                              self.__gety_data_end_time_point__())
                    if not y_data.empty:
                        time_point_list = np.array(y_data['trade_date'])
                        y = np.array(y_data['pct_change'])
                        for i in range(0, int(len(y) / ob_length)):
                            y_t = y[i * ob_length:(i + 1) * ob_length]
                            distance, path = similarity_calculation(x, y_t, dist=euclidean)
                            result_dis.append(distance)
                            result_dt.append(time_point_list[(i + 1) * ob_length - 1])
                            result_ts.append(stock)
            result = pd.DataFrame({'ts_code': result_ts, 'distance': result_dis, 'time_point': result_dt})
            return result.sort_values(by='distance', axis=0, ascending=True)

    def __count_quota__(self):
        first_pct_change = []
        second_pct_change = []
        third_pct_change = []
        for index, row in self.__similar_stock__.iterrows():
            stock = row['ts_code']
            time = row['time_point']
            e_t = datetime.strptime(time, "%Y%m%d") + timedelta(days=30)
            data = sd.get_daily_bar(stock, time, datetime.strftime(e_t, "%Y%m%d"))
            if (not data.empty) and len(data)>=3:
                x = np.array(data['pct_change'])
                first_pct_change.append(x[0])
                second_pct_change.append(x[1])
                third_pct_change.append(x[2])
        self.__first_pct_change__ = np.array(first_pct_change)
        self.__second_pct_change__ = np.array(second_pct_change)
        self.__third_pct_change__ = np.array(third_pct_change)

    def init(self):
        data = self.__getSimilarStock__()
        if self.__error__:
            pass
        else:
            self.__similar_stock__ = data[0:10]
            self.__count_quota__()

    def getExpectedReturn(self):
        if self.__error__:
            return None
        else:
            one = np.mean(self.__first_pct_change__)
            two = np.mean(self.__second_pct_change__)
            three = np.mean(self.__third_pct_change__)
            return {"one": one, "two": two, "three": three}

    def getVotes(self):
        if self.__error__:
            return None
        else:
            one_up = len(
                self.__first_pct_change__[(self.__first_pct_change__ > 0.01)])
            one_blc = len(
                self.__first_pct_change__[(self.__first_pct_change__ >= -0.01) & (self.__first_pct_change__ <= 0.01)])
            one_down = len(
                self.__first_pct_change__[(self.__first_pct_change__ < -0.01)])
            two_up = len(
                self.__second_pct_change__[(self.__second_pct_change__ > 0.01)])
            two_blc = len(
                self.__second_pct_change__[
                    (self.__second_pct_change__ >= -0.01) & (self.__second_pct_change__ <= 0.01)])
            two_down = len(
                self.__second_pct_change__[(self.__second_pct_change__ < -0.01)])
            three_up = len(
                self.__third_pct_change__[(self.__third_pct_change__ > 0.01)])
            three_blc = len(
                self.__third_pct_change__[(self.__third_pct_change__ >= -0.01) & (self.__third_pct_change__ <= 0.01)])
            three_down = len(
                self.__third_pct_change__[(self.__third_pct_change__ < -0.01)])
            return {"one": [one_up, one_blc, one_down], "two": [two_up, two_blc, two_down],
                    "three": [three_up, three_blc, three_down]}

    def getSimilarStocks(self):
        if self.__error__:
            return None
        else:
            result=[]
            for index, row in self.__similar_stock__.iterrows():
                stock = row['ts_code']
                time = row['time_point']
                distance=row['distance']
                result.append({"ts_code":stock,"time_point":time,"distance":distance})
            return result


class SimilarityShortTerm(object):
    ts_code = None
    prediction_time_point = None
    matching_period = 20
    matching_range = 10
    __ob_window__ = 30
    __error__ = False
    __similar_stock__ = None
    __trend_line__ = None

    def __init__(self, ts_code, prediction_time_point, matching_period=20, matching_range=10):
        self.ts_code = ts_code
        self.prediction_time_point = prediction_time_point
        self.matching_period = matching_period
        self.matching_range = matching_range

    def __getx_data_start_time_point__(self):
        c_t = datetime.strptime(self.prediction_time_point, "%Y%m%d")
        s_t = c_t - timedelta(days=self.matching_period)
        return datetime.strftime(s_t, "%Y%m%d")

    def __gety_data_start_time_point__(self):
        c_t = datetime.strptime(self.prediction_time_point, "%Y%m%d")
        s_t = c_t.replace(year=c_t.year - self.matching_range)
        return datetime.strftime(s_t, "%Y%m%d")

    def __gety_data_end_time_point__(self):
        c_t = datetime.strptime(self.prediction_time_point, "%Y%m%d")
        e_t = c_t - timedelta(days=self.__ob_window__)
        return datetime.strftime(e_t, "%Y%m%d")

    # 取出除自己外最相似的股票时间段
    def __getSimilarStock__(self):
        result_dis = []
        result_dt = []
        result_ts = []
        stock_list = sd.get_similar_industry_stock(self.ts_code)
        x_data = sd.get_daily_bar(self.ts_code, self.__getx_data_start_time_point__(), self.prediction_time_point)
        if x_data.empty:
            self.__error__ = True
            return None
        else:
            x = np.array(x_data['pct_change'])
            ob_length = len(x)
            for index, row in stock_list.iterrows():
                stock = row['ts_code']
                if stock != self.ts_code:
                    y_data = sd.get_daily_bar(stock, self.__gety_data_start_time_point__(),
                                              self.__gety_data_end_time_point__())
                    if not y_data.empty:
                        time_point_list = np.array(y_data['trade_date'])
                        y = np.array(y_data['pct_change'])
                        for i in range(0, int(len(y) / ob_length)):
                            y_t = y[i * ob_length:(i + 1) * ob_length]
                            distance, path = similarity_calculation(x, y_t, dist=euclidean)
                            result_dis.append(distance)
                            result_dt.append(time_point_list[(i + 1) * ob_length - 1])
                            result_ts.append(stock)
            result = pd.DataFrame({'ts_code': result_ts, 'distance': result_dis, 'time_point': result_dt})
            return result.sort_values(by='distance', axis=0, ascending=True)

    def __count_quota__(self):
        trend_line_result = {}
        for index, row in self.__similar_stock__.iterrows():
            stock = row['ts_code']
            time = row['time_point']
            e_t = datetime.strptime(time, "%Y%m%d") + timedelta(days=self.__ob_window__)
            data = sd.get_daily_bar(stock, time, datetime.strftime(e_t, "%Y%m%d"))
            if not data.empty:
                x = list(data['close'])
                trend_line_result.setdefault(stock, x)
        self.__trend_line__ = trend_line_result

    def init(self):
        data = self.__getSimilarStock__()
        if self.__error__:
            pass
        else:
            self.__similar_stock__ = data[0:3]
            self.__count_quota__()

    def getTrendLine(self):
        if self.__error__:
            return None
        else:
            return self.__trend_line__

    def getSimilarStocks(self):
        if self.__error__:
            return None
        else:
            result = {}
            for index, row in self.__similar_stock__.iterrows():
                result.setdefault(row['ts_code'], row['distance'])
            return result


class SimilarHistory(object):
    ts_code = None
    prediction_time_point = None
    matching_period = 30
    matching_range = 10
    __ob_window__ = 30
    __error__ = False
    __similar_stock__ = None
    __trend_line__ = None

    def __init__(self, ts_code, prediction_time_point, matching_period=30, matching_range=10):
        self.ts_code = ts_code
        self.prediction_time_point = prediction_time_point
        self.matching_period = matching_period
        self.matching_range = matching_range

    def __getx_data_start_time_point__(self):
        c_t = datetime.strptime(self.prediction_time_point, "%Y%m%d")
        s_t = c_t - timedelta(days=self.matching_period)
        return datetime.strftime(s_t, "%Y%m%d")

    def __gety_data_start_time_point__(self):
        c_t = datetime.strptime(self.prediction_time_point, "%Y%m%d")
        s_t = c_t.replace(year=c_t.year - self.matching_range)
        return datetime.strftime(s_t, "%Y%m%d")

    def __gety_data_end_time_point__(self):
        c_t = datetime.strptime(self.prediction_time_point, "%Y%m%d")
        e_t = c_t - timedelta(days=self.__ob_window__)
        return datetime.strftime(e_t, "%Y%m%d")

    # 取出自己相似的股票时间段
    def __getSimilarStock__(self):
        result_dis = []
        result_sdt = []
        result_edt = []
        x_data = sd.get_daily_bar(self.ts_code, self.__getx_data_start_time_point__(), self.prediction_time_point)
        if x_data.empty:
            self.__error__ = True
            return None
        else:
            x = np.array(x_data['pct_change'])
            ob_length = len(x)
            y_data = sd.get_daily_bar(self.ts_code, self.__gety_data_start_time_point__(),
                                      self.__gety_data_end_time_point__())
            if not y_data.empty:
                time_point_list = np.array(y_data['trade_date'])
                y = np.array(y_data['pct_change'])
                for i in range(0, len(y) - ob_length + 1):
                    y_t = y[i:i + ob_length]
                    distance, path = similarity_calculation(x, y_t, dist=euclidean)
                    result_dis.append(distance)
                    result_sdt.append(time_point_list[i])
                    result_edt.append(time_point_list[i + ob_length - 1])
            result = pd.DataFrame(
                {'distance': result_dis, 'start_time_point': result_sdt, 'end_time_point': result_edt})
            return result.sort_values(by='distance', axis=0, ascending=True)

    def __count_quota__(self):
        trend_line_result = {}
        for index, row in self.__similar_stock__.iterrows():
            time = row['end_time_point']
            s_t = row['start_time_point']
            e_t = datetime.strptime(time, "%Y%m%d") + timedelta(days=self.__ob_window__)
            data = sd.get_daily_bar(self.ts_code, s_t, datetime.strftime(e_t, "%Y%m%d"))
            if not data.empty:
                x = list(data['close'])
                t = list(data['trade_date'])
                trend_line_result.setdefault("close", x)
                trend_line_result.setdefault("timeline", t)
        self.__trend_line__ = trend_line_result

    def init(self):
        data = self.__getSimilarStock__()
        if self.__error__:
            pass
        else:
            self.__similar_stock__ = data[0:1]
            self.__count_quota__()

    def getTrendLine(self):
        if self.__error__:
            return None
        else:
            return self.__trend_line__

    def getSimilarDuration(self):
        if self.__error__:
            return None
        else:
            start = None
            end = None
            for index, row in self.__similar_stock__.iterrows():
                start = row['start_time_point']
                end = row['end_time_point']
            return {"start": start, "end": end}


class StockActivity(object):
    ts_code = None
    prediction_time_point = None
    matching_period = 120
    __error__ = False
    __similar_stock__ = None
    __activity__ = None

    def __init__(self, ts_code, prediction_time_point, matching_period=120):
        self.ts_code = ts_code
        self.prediction_time_point = prediction_time_point
        self.matching_period = matching_period

    def __get_data_start_time_point__(self):
        c_t = datetime.strptime(self.prediction_time_point, "%Y%m%d")
        s_t = c_t - timedelta(days=self.matching_period)
        return datetime.strftime(s_t, "%Y%m%d")

    def __mark__(self, row):
        if row['pct_change'] > 2:
            return 1
        elif row['pct_change'] < -2:
            return -1
        else:
            return 0

    def __getSimilarStock__(self):
        result_dis = []
        result_ts = []
        stock_list = sd.get_similar_industry_stock(self.ts_code)
        x_data = sd.get_daily_bar(self.ts_code, self.__get_data_start_time_point__(), self.prediction_time_point)
        if x_data.empty:
            self.__error__ = True
            return None
        else:
            x_data['pct_mark'] = x_data.apply(self.__mark__, axis=1)
            x = np.array(x_data['pct_mark'])
            for index, row in stock_list.iterrows():
                stock = row['ts_code']
                if stock != self.ts_code:
                    y_data = sd.get_daily_bar(stock, self.__get_data_start_time_point__(),
                                              self.prediction_time_point)
                    if not y_data.empty:
                        y_data['pct_mark'] = y_data.apply(self.__mark__, axis=1)
                        y = np.array(y_data['pct_mark'])
                        distance, path = similarity_calculation(x, y, dist=euclidean)
                        result_dis.append(distance)
                        result_ts.append(stock)
            result = pd.DataFrame({'ts_code': result_ts, 'distance': result_dis})
            return result.sort_values(by='distance', axis=0, ascending=True)

    def __count_quota__(self):
        result = {}
        for index, row in self.__similar_stock__.iterrows():
            stock = row['ts_code']
            data = sd.get_daily_bar(stock, self.__get_data_start_time_point__(), self.prediction_time_point)
            if not data.empty:
                data['pct_mark'] = data.apply(self.__mark__, axis=1)
                x = np.array(data['pct_mark'])
                result.setdefault(stock, float(len(x[(x != 0)])) / float(len(x)))
        self.__activity__ = result

    def init(self):
        data = self.__getSimilarStock__()
        if self.__error__:
            pass
        else:
            self.__similar_stock__ = data[0:10]
            self.__count_quota__()

    def getStockActivity(self):
        if self.__error__:
            return None
        else:
            return self.__activity__

    def getSimilarStocks(self):
        if self.__error__:
            return None
        else:
            result=[]
            for index, row in self.__similar_stock__.iterrows():
                stock = row['ts_code']
                distance=row['distance']
                result.append({"ts_code":stock,"distance":distance})
            return result


class SimilarTrend(object):
    ts_code = None
    prediction_time_point = None
    matching_period = 360
    __error__ = False
    __similar_stock__ = None
    __activity__ = None

    def __init__(self, ts_code, prediction_time_point, matching_period=360):
        self.ts_code = ts_code
        self.prediction_time_point = prediction_time_point
        self.matching_period = matching_period

    def __get_data_start_time_point__(self):
        c_t = datetime.strptime(self.prediction_time_point, "%Y%m%d")
        s_t = c_t - timedelta(days=self.matching_period)
        return datetime.strftime(s_t, "%Y%m%d")

    def __mark__(self, row):
        if row['pct_change'] > 2:
            return 1
        elif row['pct_change'] < -2:
            return -1
        else:
            return 0

    def __getSimilarStock__(self):
        result_dis = []
        result_ts = []
        stock_list = sd.get_similar_industry_stock(self.ts_code)
        x_data = sd.get_daily_bar(self.ts_code, self.__get_data_start_time_point__(), self.prediction_time_point)
        if x_data.empty:
            self.__error__ = True
            return None
        else:
            x = np.array(x_data['pct_change'])
            for index, row in stock_list.iterrows():
                stock = row['ts_code']
                if stock != self.ts_code:
                    y_data = sd.get_daily_bar(stock, self.__get_data_start_time_point__(),
                                              self.prediction_time_point)
                    if not y_data.empty:
                        y = np.array(y_data['pct_change'])
                        distance, path = similarity_calculation(x, y, dist=euclidean)
                        result_dis.append(distance)
                        result_ts.append(stock)
            result = pd.DataFrame({'ts_code': result_ts, 'distance': result_dis})
            return result.sort_values(by='distance', axis=0, ascending=True)

    def __count_quota__(self):
        result = {}
        for index, row in self.__similar_stock__.iterrows():
            stock = row['ts_code']
            data = sd.get_daily_bar(stock, self.__get_data_start_time_point__(), self.prediction_time_point)
            if not data.empty:
                data['pct_mark'] = data.apply(self.__mark__, axis=1)
                x = np.array(data['pct_mark'])
                result.setdefault(stock, float(len(x[(x != 0)])) / float(len(x)))
        self.__activity__ = result

    def init(self):
        data = self.__getSimilarStock__()
        if self.__error__:
            pass
        else:
            self.__similar_stock__ = data[0:10]
            self.__count_quota__()

    def getActivityByTrend(self):
        if self.__error__:
            return None
        else:
            return self.__activity__

    def getSimilarStocks(self):
        if self.__error__:
            return None
        else:
            result=[]
            for index, row in self.__similar_stock__.iterrows():
                stock = row['ts_code']
                distance=row['distance']
                result.append({"ts_code":stock,"distance":distance})
            return result
