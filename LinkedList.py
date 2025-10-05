class Node:
    def __init__(self,value):
        self.data = value
        self.next = None 

class LL:
    def __init__(self):
        self.head = None 
        self.n = 0 
    
    def __len__(self):
        return self.n 
    
    def __str__(self):
        res = ''
        curr = self.head 
        
        while curr!=None:
            res = res + str(curr.data) + '->'
            curr = curr.next 
        
        return res[:-2] 
        
    def insert_head(self,value):
        new_node = Node(value)
        new_node.next = self.head 
        self.head = new_node
        self.n += 1 
    
    def append(self,value):
        new_node = Node(value)
        curr = self.head 
        while curr.next!=None:
            curr = curr.next 
        curr.next = new_node 
        self.n += 1 
    
    def insert_after(self,after,value):
        curr = self.head 
        new_node = Node(value)
        while curr!=None:
            if curr.data == after:
                break 
            curr = curr.next 
        
        new_node.next = curr.next 
        curr.next = new_node
        self.n += 1 
    
    def delete_head(self):
        if self.head == None:
            return 'Empty LL'
        
        self.head = self.head.next 
        self.n -= 1 
    
    def pop(self):
        if self.head == None:
            return 'Empty LL'
        curr = self.head 
        while curr.next.next != None:
            curr = curr.next 
        curr.next = None 
        self.n -= 1 
    
    def remove(self,value):
        
        if self.head.data == value:
            self.delete_head()
            return 
        
        curr = self.head 
        while curr.next!=None:
            if curr.next.data == value:
                break 
            curr = curr.next 
        if curr.next != None:
            ## mil gaya 
            curr.next = curr.next.next 
            self.n -= 1 
        else:
            return 'Item not found'
        
    def search(self,value):
        curr = self.head 
        pos = 0 
        while curr!=None:
            if curr.data == value:
                return pos 
            curr = curr.next 
            pos += 1 
            
    def __getitem__(self,index):
        curr = self.head 
        pos = 0 
        while curr!=None:
            if pos==index:
                return curr.data
            curr = curr.next 
            pos += 1 
        
        

L = LL()
L.insert_head(1)
L.insert_head(2)
L.append(3)
L.append(4)
L.insert_after(4,5)
L.insert_after(1,1.5)
print(L)
print('Length: ',len(L))
L.delete_head()
print(L)
L.pop()
print(L)
L.remove(1.5)
print(L)
print(L.search(3))
print(L[1])          
