import logging
import logging_setup


logger = logging_setup.set_logger(__name__)

def process_request(request_id, user_id, action):
    logger.info("start action:=%s user id:=%s requst id:=%s", action, user_id, request_id)

    if not action:
        logger.warning("empty action in user id:=%s requst id=%s", user_id, request_id)
        return

    logger.info("action=%s in user id=%s completed. requst id=%s", action, user_id, request_id)

process_request(12245687442, 5252, "")
process_request(122452, 12356, "loging")
    