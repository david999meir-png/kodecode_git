import logging
import json
from datetime import datetime
import logging_setup


logging.basicConfig(level=logging.DEBUG, format='%(levelname)s | %(messege)s')
logger = logging.getLogger(__name__)

#  pdf הערה לבודק - התשובות הראשונות נכתבו על הקובץ 

# exersice 6

def process_payment(user_id, amount):
    logger.info("Starting payment for user=%s", user_id)

    if amount <= 0:
        logger.error('ERROR: Invalid amount=%s', amount)
        return
    
    if amount > 10000:
            logger.warning('WARNING: Large transaction=%s', amount)
    logger.info('Payment of=%s completed for user=%s', amount , user_id)


# exersice 7
file_handler = logging.FileHandler("payments.log", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def write_log(level, module_name, message):
    logger = logging.getLogger(module_name)

    if level == "INFO":
        logger.info(message)
    
    if level == "ERROR":
         logger.error(message)
    
    if level == "WARNING":
         logger.warning(message)

write_log("INFO", __name__, "stock update!")
write_log("WARNING", __name__, "stock over!")
write_log("ERROR", __name__, "stock doesn't found!")



# exersice 8
def read_config(filepath):
    logger.debug("check filename=%s", filepath)
    try:
        with open(filepath) as f:
            data = f.read()
            logger.debug("read done from file=%s", filepath)
            return data
    except FileNotFoundError:
        logger.exception("filename=%s not found.", filepath)
        return None

# exersice 9
def write_structured_log(level, module, message, **extra):

    log_dict = { 
                "timestamp": datetime.utcnow().isoformat(),
                "level": level,
                "module": module,
                 "message": message,
                 **extra
                }
    
    str_dict = json.dumps(log_dict, ensure_ascii=False)
    logger.level(str_dict)


# exersice 12
def register_user(email, password, age):
    logger.debug('start register user')
    if age < 18:
        logger.error('low age=%s', age)
        return
    logger.info('ok email=%s password=%s', email, bool(password))
    logger.info('completed seccessfuly')


# exercise 13
logger_3 = logging_setup.set_logger(__name__)


# exersice 14

import exercise_14
