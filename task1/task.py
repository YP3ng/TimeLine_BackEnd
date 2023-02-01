from celery import shared_task
from celery.result import AsyncResult
from time import sleep
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)

@shared_task(bind=True, name='tasks.add')
def add(self, input):
    sleep(5) # Simulate expensive operations
    logger.info("add 100")

    # Info about current task
    #logger.info(self.request)

    # FIXME:Update_state not working
    # Issue: State gets override by built-in state, 
    # and RPC backend doesn't store the states in-progress
    # Solution: Select other backend, maybe Redis or DB
    logger.info(self.AsyncResult(self.request.id).state)

    self.update_state(
        state= "CUSTOM", 
        meta={'input': input, 'result': input+100}
    )

    logger.info(self.AsyncResult(self.request.id).state) # PENDING
    return input + 100


@shared_task
def multiply(input):
    sleep(5) # Simulate expensive operations
    logger.info("multiply by 10")
    return input * 10