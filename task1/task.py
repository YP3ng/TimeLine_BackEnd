from celery import shared_task
from time import sleep
from celery.utils.log import get_task_logger

logger = get_task_logger('test')

@shared_task
def calculate(input):
    sleep(20)
    logger.info("Awake!!!!!")
    return input + 100