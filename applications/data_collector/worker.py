import os

import redis
from rq import Worker, Queue, Connection

listen = ['default']

conn = redis.from_url("redis://red-cnksjben7f5s73b1v9q0:6379")

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()