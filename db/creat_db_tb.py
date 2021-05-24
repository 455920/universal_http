from app.dao.mysql_dao import MysqlDao
from app.dao.userinfo_dao import UserInfoDao, UserInfo
from app.conf.global_config import g_conf


# 创建库表
class CreateDbTb:
    DB_NAME = "test_db1"
    TB_USER = "user"
    TB_USER_PARAMS = '''uid INT(64) PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(128) NOT NULL,
    password VARCHAR(128) NOT NULL,
    number VARCHAR(32) NOT NULL,
    modify_time TIMESTAMP NOT NULL,
    create_time TIMESTAMP NOT NULL,
    status INT(8) NOT NULL,
    UNIQUE(number)'''
    TB_TEST = "test"
    TB_TEST_PARAMS = '''id INT(8)'''

    DROP_DB = "DROP DATABASE %s" % DB_NAME
    CREATE_DB = "CREATE DATABASE IF NOT EXISTS %s;" % DB_NAME
    USE_DB = "USE %s;" % DB_NAME
    CREATE_TB_TEMPLATE = "CREATE TABLE IF NOT EXISTS %s(%s);"

    CREATE_USER_TB = CREATE_TB_TEMPLATE % (TB_USER, TB_USER_PARAMS)
    CREATE_TEST_TB = CREATE_TB_TEMPLATE % (TB_TEST, TB_TEST_PARAMS)


if __name__ == "__main__":
    host = g_conf["db"]["host"]
    port = g_conf["db"]["port"]
    user = g_conf["db"]["user"]
    password = g_conf["db"]["password"]

    # 连接数据库
    db = MysqlDao(host=host, port=port, user=user, password=password)
    db.connect_db()

    # 删除库
    db.execute(CreateDbTb.DROP_DB)

    # 创建库
    db.execute(CreateDbTb.CREATE_DB)

    # 创建用户表
    db.execute_many([CreateDbTb.USE_DB, CreateDbTb.CREATE_USER_TB])

    # 创建测试表
    db.execute_many([CreateDbTb.USE_DB, CreateDbTb.CREATE_TEST_TB])
