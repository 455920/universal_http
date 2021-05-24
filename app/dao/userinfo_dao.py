import logging
from app.dao.mysql_dao import MysqlDao
from app.comm.app_error import AppError


class UserInfo:
    def __init__(self):
        self.uid = None
        self.name = None
        self.password = None
        self.number = None
        self.modify_time = None
        self.create_time = None
        self.status = None


class UserInfoDao(MysqlDao):
    def __init__(self, host, port, user, password):
        super().__init__(host, port, user, password)
        self.tb_template = "test_db1.user"

    def __del__(self):
        super().__del__()

    def get_table_name(self):
        return self.tb_template  # todo 支持分库分表

    def query(self, condition, limit=1):
        sql = " SELECT uid,name,password,number,modify_time,create_time,status FROM %s WHERE %s LIMIT %s " % (
            self.get_table_name(), condition, limit)
        res_data = super().query(sql)
        # res_len = len(res_data)
        # if res_len != limit:
        #     logging.error("query row not 1")
        #     raise Exception(AppError.ROW_NOT_ONE)

        res_list = []

        for row_data in res_data:
            userinfo = UserInfo()
            userinfo.uid = row_data[0]
            userinfo.name = row_data[1]
            userinfo.password = row_data[2]
            userinfo.number = row_data[3]
            userinfo.modify_time = row_data[4]
            userinfo.create_time = row_data[5]
            userinfo.status = row_data[6]
            res_list.append(userinfo)

        return res_list

    def insert(self, userinfo: UserInfo):
        sql = " INSERT INTO %s(uid,name,password,number, modify_time,create_time, status)" \
              " VALUES(\'%s\', \'%s\', \'%s\', \'%s\', now(), now(), 1)" % (
                  self.get_table_name(), userinfo.uid, userinfo.name, userinfo.password, userinfo.number)
        res_data = super().insert(sql)
        return res_data

    def update(self, userinfo: UserInfo, update_list=None):
        if update_list is None:
            logging.error("update updata_list is None")
            raise Exception(AppError.DB_PARAM_INVALID)
        sql = " UPDATE %s SET %s,modify_time=now()" \
              " WHERE uid='%s'" % (
                  self.get_table_name(), update_list, userinfo.uid)
        res_data = super().update(sql)
        return res_data
