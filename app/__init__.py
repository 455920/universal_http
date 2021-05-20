#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from app.main import main_blue_print
from app.user import user_blue_print


def create_http_app():
    http_app = Flask(__name__)

    http_app.register_blueprint(main_blue_print)
    http_app.register_blueprint(user_blue_print, url_prefix='/user')

    return http_app
