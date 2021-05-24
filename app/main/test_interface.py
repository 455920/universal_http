from flask import request
from app.main import main_blue_print
from app.comm.interface_base import InterfaceBase
from app.comm.app_error import AppError
from app.comm.logger import logger


class TestInterface(InterfaceBase):
    def __init__(self, rqst):
        super(TestInterface, self).__init__()
        self.rqst_ = rqst
        self.name_ = None
        self.number_ = None
        self.pwd_ = None
        self.ret_ = 0  # 返回错误码
        self.ret_info_ = ""  # 返回信息

    def parse_input(self):
        logger.info("parse_input")
        self.name_ = self.rqst_.args.get("name")
        self.number_ = self.rqst_.args.get("number")

    def set_output(self):
        logger.info("set_output")
        self.rsp["ret"] = self.ret_
        self.rsp["ret_info"] = self.ret_info_
        self.rsp["pwd"] = self.pwd_

    def do_execute(self):
        logger.info("do_execute")
        self.ret_ = AppError.OK
        self.ret_info_ = "ok"
        self.pwd_ = self.name_ + self.number_


@main_blue_print.route('/')
def test():
    obj = TestInterface(request)
    return obj.execute()
