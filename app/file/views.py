from . import file_blue_print


@file_blue_print.route('/')
def index():
    return "file"


