# 编写数据模型
import json
from flask import request, jsonify, Blueprint, redirect, url_for, render_template

from BackEnd.App import Conf
# 用户相关蓝图
user_route = Blueprint('user_route',
                       __name__,
                       static_folder='static',
                       template_folder='template',
                       url_prefix='/users')
def log_user():
    user_info = json.load(open(Conf.datasetsUrl, 'r', encoding='utf-8'))
    return user_info
@user_route.route('/checkstate', methods=['POST'],endpoint='checkstate')
def checkstate():
    """
    注册检查
    :return: 注册信息 状态，信息，数据
    """
    data = request.json
    username = data['username']
    pwd = data['pwd']
    nickname = data['nickname']
    user = log_user()
    if username in user:
        return {'state': 0, 'message': '用户名已存在', 'data': {}}
    with open(Conf.datasetsUrl,'r',encoding='utf-8') as f:
        user_data = json.load(f)
        with open(Conf.datasetsUrl,'w',encoding='utf-8') as fp:
            user_data[username]={'password':pwd,'state':0,'flag':0,'nickname':nickname}
            json.dump(user_data,fp,ensure_ascii=False,indent=2)
    return jsonify({'state': 1, 'message': '成功', 'data': {}})


@user_route.route('/login', methods=['post'], endpoint='login_state')
def login():
    """
    登陆验证
    :return:验证信息 状态 信息 数据
    """
    info = {'state': '', 'message': '', 'data': {}}
    username = request.form['username']
    password = request.form['password']
    user = log_user()
    if username in user:
        if password == user[username]['password']:
            info['state'] = 1
            info['message'] = '登陆成功'
            Conf.userShowname = user[username]['nickname']
            # 登陆成功后跳转主页面
            return redirect(url_for('routes.homePage'))
        else:
            info['state'] = 0
            info['message'] = '密码错误'
    else:
        info['state'] = 0
        info['message'] = '用户不存在'
    
    return info

@user_route.route('/register',endpoint='register')
def register():
    register_url = url_for('user_route.register')
    return render_template('register.html',register_url=register_url)