## Implement Queue Using LinkedList

class Node:
    def __init__(self,value):
        self.data = value 
        self.next = None
        
class Queue:
    def __init__(self):
        self.front= None
        self.rear = None 
        
    def enqueue(self,value):
        new_node = Node(value)
        
        if self.rear==None:
            self.front = new_node
            self.rear = self.front 
        else:
            self.rear.next = new_node
            self.rear = new_node 
        
    def dequeue(self):
        if self.front == None:
            return 'empty'
        else:
            self.front = self.front.next 
    
    def traverse(self):
        temp = self.front 
        while temp!=None:
            print(temp.data,end=' ')
            temp = temp.next 
        print()
    
    def front_item(self):
        if self.front==None:
            return 'empty'
        else:
            return self.front.data
            
    def rear_item(self):
        if self.front==None:
            return 'empty'
        else:
            return self.rear.data
    
    def size(self):
        temp = self.front 
        counter = 0
        while temp!=None:
            counter += 1
            temp = temp.next 
        return counter
        

q = Queue()
print('Intialize Queue')
print('front item: ',q.front_item())
print('rear item: ',q.rear_item())
print('-------------')

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

q.traverse()

print('size: ',q.size())
print('front item: ',q.front_item())
print('rear item: ',q.rear_item())

q.dequeue()
q.dequeue()

print('after delete -----')
q.traverse()
print('-------------')
print('front item: ',q.front_item())
print('rear item: ',q.rear_item())


