class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: Stack is empty")

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()

stack.push(8)
stack.push(3)
stack.push(34)

print("Stack:", stack.items)

top_item = stack.pop()
print("Popped:", top_item)
print("Stack after pop:", stack.items)

peeked_item = stack.peek()
print("Peeked:", peeked_item)
print("Stack size:", stack.size())








