class Node: 
    def __init__(self,value):
        self.data = value
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        return self.top == None
        
    def peek(self):
        if (self.is_empty()):
            return "stack empty"
        return self.top.data
        
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top 
        self.top = new_node
    
    def pop(self):
        if (self.is_empty()):
            return "stack empty"
        else:
            data = self.top.data 
            self.top = self.top.next
        return data 
    
    def traversal(self):
        temp = self.top 
        while(temp!=None):
            print(temp.data)
            temp = temp.next 
        
    def size(self):
        temp = self.top 
        counter = 0
        while temp!=None:
            counter+=1 
            temp = temp.next 
        return counter

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

s.traversal()
print('size of stack',s.size())
print('peek value',s.peek())

s.pop()
s.pop()

s.traversal()
print('peek value',s.peek())

print('size of stack',s.size())


        