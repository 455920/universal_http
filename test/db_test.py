from app.dao.mysql_dao import MysqlDao
from app.dao.userinfo_dao import UserInfoDao, UserInfo
from app.conf.global_config import g_conf

host = g_conf["db"]["host"]
port = g_conf["db"]["port"]
user = g_conf["db"]["user"]
password = g_conf["db"]["password"]

# 查询mysql版本
db = MysqlDao(host=host, port=port, user=user, password=password)
db.connect_db()
res = db.execute("SELECT version();")
print(res)

# 删除库表
res = db.execute("DROP DATABASE test_db1")

# 创建库表
create_sqls = ["CREATE DATABASE IF NOT EXISTS test_db1;",
               "USE test_db1;",
               "CREATE TABLE IF NOT EXISTS user("
               "uid INT(64) PRIMARY KEY AUTO_INCREMENT,"  # 用户uid
               "name VARCHAR(32) NOT NULL,"  # 姓名
               "password VARCHAR(128) NOT NULL,"  # 密码
               "number VARCHAR(32) NOT NULL,"  # 电话
               "modify_time TIMESTAMP NOT NULL,"  # 修改时间
               "create_time TIMESTAMP NOT NULL,"  # 创建时间
               "status INT(8) NOT NULL,"  # 用户状态 1: 有效, 2: 注销
               "UNIQUE(number)"
               ");"]

res = db.execute_many(create_sqls)
print(res)

# 用户插入
user_db = UserInfoDao(host=host, port=port, user=user, password=password)
userinfo = UserInfo()
userinfo.uid = "1"
userinfo.name = "a"
userinfo.password = "123456789"
userinfo.number = "123456789"
res = user_db.insert(userinfo)
print(res)

# 查询所有用户
us = user_db.query("uid='1'")
u = us[0]
print(u.uid)
print(u.name)
print(u.password)
print(u.number)
print(u.create_time)
print(u.modify_time)
print(u.status)

user_db.update(userinfo, "status=2")

# 查询用户
us = user_db.query("uid='1'")
u = us[0]
print(u.uid)
print(u.name)
print(u.password)
print(u.number)
print(u.create_time)
print(u.modify_time)
print(u.status)
