from flask import Blueprint

user_blue_print = Blueprint('user', __name__)
from . import views
