#!/usr/bin/env python

import schedule
import time
from celery import Celery
from scraper import scrape

HOST = 'amqp://guest@localhost'
QUEUE = 'celery_pages'

app = Celery(QUEUE, HOST)

urls = [ "http://ebay.to/1G163Lh" ]

def produce():
    for url in urls:
        scrape.delay(url)
        print("* Submitted: [%s]" % (url))

schedule.every(2).seconds.do(produce)

while True:
    schedule.run_pending()
    time.sleep(1)
