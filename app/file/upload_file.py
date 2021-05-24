from . import file_blue_print
from app.comm.logger import logger


@file_blue_print.route('/md5')
def md5():
    logger.info("md5")
    return "md5"
