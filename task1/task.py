from celery.decorators import task

@task(name="calculate")
def calculate(x, y):
    res = x + y
    return res