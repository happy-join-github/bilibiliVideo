from flask import Flask
from .config import Conf
from .views import routes
from .models import user_route
import json
import os


def setCookies():
    from BackEnd.App.config import Conf
    json_data_path = Conf.setcookiesPath
    
    if not os.path.exists(json_data_path):
        data = open(Conf.getcookiesPath, 'r', encoding='utf-8').read().replace('"', '').replace("'",'').strip().split(';')
        dic = {val.split('=')[0].strip(): val.split('=')[1] for key, val in enumerate(data)}
        json_data = {'flag': 0, 'cookies': dic}
        
        with open(json_data_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f)
        
    else:
        # 替换cookies
        data = open(Conf.getcookiesPath, 'r', encoding='utf-8').read().replace('"', '').replace("'",'').strip().split(';')
        if data!=['']:
            dic = {val.split('=')[0].strip(): val.split('=')[1] for key, val in enumerate(data)}
            json_data = json.load(open(json_data_path,'r',encoding='utf-8'))
            json_data['cookies'] = dic
            with open(json_data_path, 'w', encoding='utf-8') as f:
                json.dump(json_data, f)
        else:
            raise '请获取bilibili cookies'
        
    return json_data['cookies']



def create():
    app = Flask(__name__)
    # 加载cookies
    cookies = setCookies()
    # 注册蓝图
    app.register_blueprint(routes)
    app.register_blueprint(user_route)
    return app,cookies




    