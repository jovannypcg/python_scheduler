import pika         # RabbitMQ client library
import schedule     # Schedules processes
import time         # To use the sleep method

# List of urls to send via RabbitMQ
URLS = ['http://ebay.to/1G163Lh',
        'http://www.google.com.mx',
        'http://localhost:8080']

# The host in which RabbitMQ is running
HOST = 'localhost'

# The name of the queue
QUEUE = 'urls'

print 'Connecting to RabbitMQ...\n'

# Starting the connection
# Creation of the channel based on the connection
# The queue is declared
connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
channel = connection.channel()
channel.queue_declare(queue=QUEUE)

""" Sends the list of urls to RabbitMQ """
def produce():
    for url in URLS:
        print '* Pushed: [%s]' % url
        channel.publish(exchange='',
                        routing_key=QUEUE,
                        body=url)

# Every 2 seconds the method 'produce' is executed
schedule.every(2).seconds.do(produce)

# Runs the scheduler as a daemon
while True:
    schedule.run_pending()
    time.sleep(1)

# The connection is closed
connection.close()
