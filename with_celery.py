from celery import Celery

# The host in which RabbitMQ is running
HOST = 'amqp://guest@localhost'

app = Celery('pages_celery', broker=HOST)

@app.task
def work(msg):
    print msg

# To execute the task:
#
# $ python
# >>> from with_celery import work
# >>> work.delay('Hi there!!')
