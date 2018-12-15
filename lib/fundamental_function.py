from fastdtw import fastdtw
import base64
#一维相似度计算
def similarity_calculation(x, y, dist):
    if len(x) == len(y):
        return dist(x, y), None
    else:
        return fastdtw(x, y, dist=dist)

def dict_to_sql(dict):
    tempstr = str(dict)
    binary = base64.b64encode(tempstr)
    return binary


def sql_to_dict(bin):
    tempstr = base64.b64decode(bin)
    dict = eval(tempstr)
    return dict
