class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next  = None
        
class LL:
    def __init__(self):
        self.head = None 
    
    def add(self,key,value):
        new_node = Node(key,value)
        if self.head==None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next 
            temp.next = new_node 
        
    def delete_head(self):
        if self.head == None:
            return 'Empty'
        else:
            self.head = self.head.next 
        
        
    
    def remove(self,key):
        if self.head.key == key:
            self.delete_head()
            return 
        
        if self.head == None:
            return 'empty'
            
        temp = self.head
        while temp!=None:
            if temp.next.key == key:
                break 
            temp = temp.next 
            
        temp.next = temp.next.next
    
    def traverse(self):
        temp = self.head 
        while temp!=None:
            print(temp.key,'-->',temp.value,end=' ')
            temp = temp.next 
    
    def search(self,key):
        temp = self.head
        pos = 0
        while temp!=None:
            if temp.key == key:
                return pos
            temp = temp.next 
            pos += 1 
        return -1 
        
    def size(self):
        temp = self.head 
        counter = 0
        while temp!=None:
            counter += 1 
            temp = temp.next 
        return counter 
    
    def get_node_at_index(self,index):
        temp = self.head 
        counter = 0
        while temp!=None:
            if counter == index:
                return temp 
            temp = temp.next
            counter += 1 
        
        
        
class Dict:
    def __init__(self,capacity):
        self.size = 0
        self.capacity = capacity 
        self.buckets = self.make_array(self.capacity)
    
    def make_array(self,capacity):
        L = []
        
        for i in range(capacity):
            L.append(LL())
        return L
    
    def put(self,key,value):
        bucket_index = self.hash_function(key)
        
        node_index = self.get_node_index(bucket_index,key)
        
        if node_index == -1:
            self.buckets[bucket_index].add(key,value)
            self.size += 1 
            
            load_factor = self.size/self.capacity
            print(load_factor)
            
            if (load_factor>=2):
                self.rehash()
            
        else:
            node = self.buckets[bucket_index].get_node_at_index(bucket_index)
            node.value = value 
    
    def __setitem__(self,key,value):
        return self.put(key,value)
    
    def get(self,key):
        bucket_index = self.hash_function(key)
        
        node_index = self.buckets[bucket_index].search(key)
        
        if node_index==-1:
            return 'Not found'
        else:
            node = self.buckets[bucket_index].get_node_at_index(bucket_index)
            return node.value
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __delitem__(self,key):
        bucket_index = self.hash_function(key)
        self.buckets[bucket_index].remove(key)
        
    def hash_function(self,key):
        return abs(hash(key)) % self.capacity

    def rehash(self):
        self.capacity = self.capacity * 2
        self.size = 0
        A = self.make_array(self.capacity)
        old_buckets = self.buckets 
        
        for i in range(len(old_buckets)):
            for j in range(i.size()):
                node = i.get_node_at_index(j)
                node_key = node.key 
                node_value = node.value 
                self.put(node_key,node_value)
                
    def get_node_index(self,bucket_index,key):
        node_index = self.buckets[bucket_index].search(key)
        return node_index
    
    def __str__(self):
        for i in self.buckets:
            i.traverse()
        return ''
    
    def __len__(self):
        return self.size
        
d1 = Dict(3)

d1.put('python',100)
d1.put('java',200)
d1.put('c++',300)
d1.put('go',400)
d1.put('ruby',500)

print(d1)
print('length: ',len(d1))

print(d1.get('python'))
print(d1['java'])

del d1['c++']

print(d1)