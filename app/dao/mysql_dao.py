import pymysql
import logging


class MysqlDao:
    def __init__(self, host, port, user, password):
        self.host_ = host
        self.port_ = port
        self.user_ = user
        self.password_ = password
        self.charset_ = "utf8"
        self.connect_ = None

    def __del__(self):
        self.close_db()

    def connect_db(self):
        self.connect_ = pymysql.connect(host=self.host_,
                                        user=self.user_,
                                        port=self.port_,
                                        password=self.password_,
                                        charset=self.charset_)
        logging.info("connect db %s", self.host_)

    def close_db(self):
        if self.connect_ is not None:
            self.connect_.close()
            self.connect_ = None
        logging.info("close db %s", self.host_)

    def execute(self, cmd):
        print(cmd)
        if self.connect_ is None:
            self.connect_db()
        cur = self.connect_.cursor()
        cur.execute(cmd)
        cur.close()

    def update(self, cmd):
        print(cmd)
        if self.connect_ is None:
            self.connect_db()
        cur = self.connect_.cursor()
        res_data = None
        # try:
        cur.execute(cmd)
        res_data = cur.fetchall()
        self.connect_.commit()
        # except Exception as e:
        #     self.connect_.rollback()
        #     cur.close()

        return res_data

    def query(self, cmd):
        print(cmd)
        if self.connect_ is None:
            self.connect_db()
        cur = self.connect_.cursor()
        cur.execute(cmd)
        res_data = cur.fetchall()
        cur.close()
        return res_data

    def insert(self, cmd):
        print(cmd)
        if self.connect_ is None:
            self.connect_db()
        cur = self.connect_.cursor()
        res_data = None
        # try:
        cur.execute(cmd)
        res_data = cur.fetchall()
        self.connect_.commit()
        # except Exception as e:
        #     self.connect_.rollback()
        #     cur.close()

        return res_data

    def execute_many(self, cmds):
        if self.connect_ is None:
            self.connect_db()
        cur = self.connect_.cursor()
        for cmd in cmds:
            cur.execute(cmd)
            print(cur.fetchall())
