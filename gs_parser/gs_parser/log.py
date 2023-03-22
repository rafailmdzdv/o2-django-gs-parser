import logging
import sys

from gs_parser import settings


def logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '[%(levelname)s] %(asctime)s-%(name)s - %(message)s'
    )
    stream_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.FileHandler(settings.ERROR_PATH)
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger


log = logger()
