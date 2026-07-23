class library:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def is_empty(self):
        return self.top is None
    def push(self,data):
        new_node=library(data)
        new_node.next=self.top
        self.top=new_node
        print(f"{data} is pushed")
    def pop(self):
        if self.is_empty():
            return None
        popped_data=self.top.data
        self.top=self.top.next
        return popped_data
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data
stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("peek:",stack.peek())
print("pop:",stack.pop())
