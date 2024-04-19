from multiprocessing import Queue

customQueue = Queue(maxsize=3)
customQueue.put(10)
print(customQueue.get())