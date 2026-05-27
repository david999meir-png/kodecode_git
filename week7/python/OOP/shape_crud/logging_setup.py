import logging

def set_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(level=logging.DEBUG)

    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("app.log")

    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')

    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger


if __name__ == "__main__":
    logger = set_logger(__name__)

    logger_1 = set_logger("logger_a")
    logger_1.info("one")

    logger_2 = set_logger("logger_b")
    logger_2.info("two")
