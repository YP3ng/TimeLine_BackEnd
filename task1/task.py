from celery import shared_task

@shared_task
def calculate(input):
    return input + 1