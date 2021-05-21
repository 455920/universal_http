from . import user_blue_print


@user_blue_print.route('/reg', methods=['GET', 'POST'])
def reg():
    return "this is reg"
