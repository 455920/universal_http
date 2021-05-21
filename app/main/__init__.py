from flask import Blueprint
main_blue_print = Blueprint('main', __name__)
from . import test_interface
