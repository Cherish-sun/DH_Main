# -*- coding:utf-8 -*-
from .app import Flask
from logging.handlers import RotatingFileHandler
from .app import Flask
import logging

"""
    设置日志
"""
logging.basicConfig(level=logging.INFO)
file_log_handler = RotatingFileHandler("./logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
file_log_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_log_handler)


def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='')


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app
