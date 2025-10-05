## Stack Implementation Using Array 

class Stack:
    def __init__(self,size):
        self.size = size 
        self.stack = [None] * self.size
        self.top = -1 
    
    def push(self,value):
        if self.top == self.size -1:
            return 'overflow'
        else:
            self.top += 1 
            self.stack[self.top] = value 
    
    def pop(self):
        if self.top == -1:
            return 'empty stack'
        else:
            data = self.stack[self.top]
            self.top -= 1 
            
        return data 
    
    def peek(self):
        if self.top == -1:
            return 'empty stack'
        else:
            peek_value = self.stack[self.top]
        return peek_value
        
    def traverse(self):
        for i in range(self.top+1):
            print(self.stack[i],end=' ')
    
    def __len__(self):
        counter = 0
        for i in range(self.top+1):
            counter += 1 
        return counter
            

s = Stack(3)

s.push(1)
s.push(2)
s.push(3)


s.traverse()

print('length of stack: ',len(s))
s.pop()

print()

print('after pop ----')
s.traverse()

print('peek: ',s.peek())
print('length of stack: ',len(s))


