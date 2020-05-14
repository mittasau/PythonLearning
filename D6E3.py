import queue

def insert(q): 
    #insert items at the head of the queue 
    for x in range(5):
        q.put(str(x))

def remove(q): 
    #remove items from the head of the queue 
    while not q.empty():
        print(q.get(), end=" ")
    print("\n")


queue_1 = queue.Queue()
insert(queue_1)
remove(queue_1)
queue_2 = queue.LifoQueue()
insert(queue_2)
remove(queue_2)