import queue as q

customQueue = q.Queue(maxsize = 3)

print(customQueue.empty())
customQueue.put(10)
customQueue.put(20)
customQueue.put(30)
print(customQueue.full())
print(customQueue.get())
print(customQueue.qsize())