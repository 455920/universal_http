from . import user_blue_print
from app.comm.logger import logger


@user_blue_print.route('/reg', methods=['GET', 'POST'])
def reg():
    logger.info("this is reg")
    return "this is reg"
