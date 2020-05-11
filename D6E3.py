import queue
q = queue.Queue()
#insert items at the end of the queue 
for x in range(5):
    q.put(str(x))
#remove items from the head of the queue 
while not q.empty():
    print(q.get(), end=" ")
print("\n")


q = queue.LifoQueue()
#insert items at the head of the queue 
for x in range(5):
    q.put(str(x))
#remove items from the head of the queue 
while not q.empty():
    print(q.get(), end=" ")
print("\n")