#!/usr/bin/env python

import requests
from BeautifulSoup import BeautifulSoup
from celery import Celery

HOST = 'amqp://guest@localhost'
QUEUE = 'celery_pages'

app = Celery(QUEUE, broker=HOST)

@app.task
def scrape(url):
    print "-> Starting: [%s]" % url
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    print "-> Extracted: %s" % soup.html.head.title
    print "-> Done: [%s]" % url
