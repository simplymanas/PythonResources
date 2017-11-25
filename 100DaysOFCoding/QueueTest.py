from QueueModule import Queue

mq = Queue()

mq.enqueue(5)

mq.enqueue(4)

for n in mq.items:
    print(n)

