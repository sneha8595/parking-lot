import logging
import traceback

logging.basicConfig(level='INFO')
logger = logging.getLogger()


def log_request(message):
    try:
        logger.info(message)
    except Exception as e:
        print(traceback.format_exception_only(etype=type(e), value=e)[0])
        pass
