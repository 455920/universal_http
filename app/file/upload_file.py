from . import file_blue_print


@file_blue_print.route('/md5')
def md5():
    return "md5"
