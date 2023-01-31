from celery import shared_task, current_task
from time import sleep
from celery.utils.log import get_task_logger


logger = get_task_logger('test')

@shared_task
def add(input):
    sleep(5) # Simulate expensive operations
    logger.info("add 100")

    # TODO:Update_state not working
    # Possible issue: RPC backend can't retrieve data twice
    # Possible solution: Change backend structure to redis
    current_task.update_state(
        state= "CUSTOM", 
        meta={'input': input, 'result': input+100}
    )
    return input + 100


@shared_task
def multiply(input):
    sleep(5) # Simulate expensive operations
    logger.info("multiply by 10")
    return input * 10