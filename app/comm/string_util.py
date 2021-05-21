import hashlib


class StringUtil:
    # 生成MD5
    def gen_md5(self, src_str: str):
        # 创建md5对象
        hl = hashlib.md5()

        hl.update(src_str.encode(encoding='utf-8'))
        return hl.hexdigest()

    def valid_str(self, src, min_len, max_len):
        if src is None:
            return False
        str_len = len(src)
        if str_len >= min_len and str_len <= max_len:
            return True
        return False
