from collections import deque

customQueue = deque(maxlen = 3)
print(customQueue)


customQueue.append(10)
customQueue.append(20)
customQueue.append(30)
customQueue.append(40)
print(customQueue)
customQueue.popleft()
# print(customQueue.clear())
print(customQueue)