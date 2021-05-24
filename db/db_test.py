from app.dao.userinfo_dao import UserInfoDao, UserInfo
from app.conf.global_config import g_conf

host = g_conf["db"]["host"]
port = g_conf["db"]["port"]
user = g_conf["db"]["user"]
password = g_conf["db"]["password"]

# 连接db
user_db = UserInfoDao(host=host, port=port, user=user, password=password)


userinfo = UserInfo()
userinfo.uid = "6"
userinfo.name = "a"
userinfo.password = "123456783"
userinfo.number = "123456756"
# 插入数据
res = user_db.insert(userinfo)
print(res)

# 查询所有符合条件的用户
us = user_db.query("status='1'", limit=10)
for u in us:
    u = us[0]
    print(u.uid, u.name, u.password, u.number, u.create_time, u.modify_time, u.status)

user_db.update(userinfo, "status=2")

# 查询用户
us = user_db.query("uid='1'", limit=2)
for u in us:
    u = us[0]
    print(u.uid, u.name, u.password, u.number, u.create_time, u.modify_time, u.status)

