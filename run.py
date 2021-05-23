import logging
from app import create_http_app

http_app = create_http_app()

if __name__ == '__main__':
    logging.info("main")
    http_app.run()

