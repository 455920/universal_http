from . import main_blue_print


@main_blue_print.route('/')
def index():
    return "hello world"


@main_blue_print.route('/test')
def test():
    return "this is test"
