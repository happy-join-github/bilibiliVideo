# 编写数据模型
import json

from BackEnd.App import Conf


def log_user():
    user_info = json.load(open(Conf.datasetsUrl, 'r', encoding='utf-8'))
    
    return user_info
