from flask import Blueprint, render_template
from BackEnd.App import Conf

# 基础蓝图
routes = Blueprint('routes',
                   __name__,
                   static_folder='static',
                   template_folder='template',
                   url_prefix='/')


@routes.route('/', endpoint='index')
def index():
    return render_template('login.html')


@routes.route('/home', endpoint='homePage')
def home():
    return render_template('index.html', username=Conf.userShowname)

@routes.route('/explain',endpoint='explain')
def explainPage():
    return render_template('explain.html')
