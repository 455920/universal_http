from flask import Blueprint

file_blue_print = Blueprint('file', __name__)

from app.file import upload_file
