class stack:
    def __init__ (self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
        print(f"{item} is pushed")
    def pop(self):
        if self.is_empty():
            return "stack Underflow"
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
    def display(self):
        print("Stack elements:",self.stack)
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(50)
s.pop()
s.display()
print("top element:",s.peek())