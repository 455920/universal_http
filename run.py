import logging
from app import create_http_app
from app.conf.global_config import g_conf

http_app = create_http_app()

if __name__ == '__main__':
    logging.info("main")
    http_app.run(host=g_conf["server"]["host"], port=g_conf["server"]["port"])

