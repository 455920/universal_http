# 错误码

class AppError:
    OK = 0  # ok
    # 数据库错误以9开头
    DB_ROW_NOT_ONE = 900  # 结果行数不为1
    DB_PARAM_INVALID = 901  # 参数不合法
