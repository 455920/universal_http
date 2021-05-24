#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from flask import Flask
from app.main import main_blue_print
from app.user import user_blue_print
from app.file import file_blue_print
from app.conf.global_config import g_conf
from app.comm.logger import logger


def create_http_app():
    logger.info("create_http_app")
    # 初始化日志
    http_app = Flask(__name__)

    http_app.register_blueprint(main_blue_print)
    http_app.register_blueprint(user_blue_print, url_prefix='/user')
    http_app.register_blueprint(file_blue_print, url_prefix='/file')

    return http_app
