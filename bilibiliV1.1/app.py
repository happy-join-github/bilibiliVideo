from flask import Flask, request, redirect, url_for, render_template,jsonify
from flask_cors import CORS

from utils.loadfile import logfile
app = Flask(__name__,static_folder='static')
# 解决跨域的问题
CORS(app)
# 访问主页面
@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    """
    # 登陆验证
    :return: 验证信息 状态、信息、数据
    """
    data={'state':'','message':'','data':{}}
    username = request.form['username']
    password = request.form['password']
    user = logfile()
    if username in user:
        if password == user[username]:
            data['state'] = 1
            data['message'] = '登陆成功'
            # 登陆成功后跳转主页面
            return redirect(url_for('home'))
        else:
            data['state'] = 0
            data['message'] = '密码错误'
    else:
        data['state'] = 0
        data['message'] = '用户不存在'
    
    print(f"Username: {username}, Password: {password}")
    
    return data

@app.route('/index')
def home():
    return render_template('index.html')

# 注册页面
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/checkstate', methods=['POST'])
def checkstate():
    """
    # 注册检查
    :return: 注册信息 状态，信息，数据
    """
    # 接收发送过来的json数据
    data = request.json
    username = data['username']
    pwd = data['pwd']
    user = logfile()
    if username in user:
        return {'state': 0, 'message': '用户名已存在', 'data': {}}
    with open('dataset/user.txt', 'a', encoding='utf-8') as f:
        f.write(f'{username} {pwd}\n')
    return jsonify({'state': 1, 'message': '成功', 'data': {}})

    

app.run(host='127.0.0.1',port=5000)
