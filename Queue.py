class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Error: Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Error: Queue is empty")

    def size(self):
        return len(self.items)

queue = Queue()

queue.enqueue(9)
queue.enqueue(80)
queue.enqueue(45)

print("Queue:", queue.items)

front_item = queue.dequeue()
print("Dequeued:", front_item)
print("Queue after dequeue:", queue.items)

peeked_item = queue.peek()
print("Peeked:", peeked_item)
print("Queue size:", queue.size())