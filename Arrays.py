import ctypes 

class List:
    def __init__(self):
        self.size  = 1 
        self.n = 0
        self.A = self.__make_array(self.size)
    
    def __len__(self):
        return self.n
        
    def __str__(self):
        res = ''
        for i in range(self.n):
            res = res + str(self.A[i]) + ','
        return '[' + res[:-1] + ']'
        
    def append(self,item):
        if self.n == self.size:
            self.__resize_array(self.size*2)
        self.A[self.n]=item 
        self.n += 1 
    
    def pop(self):
        if self.n == 0:
            return 'Empty array'
        print(self.A[self.n-1])
        self.n -= 1 
    
    def __getitem__(self,index):
        if isinstance(index,int):
            if index<0:
                index = self.n + index 
            if 0<= index < self.n:
                return self.A[index]
            return 'IndexError'
        if isinstance(index,slice):
            start,stop,step = index.indices(self.n)
            result = [self.A[i] for i in range(start,stop,step)]
            return result 
    
    def __setitem__(self,index,value):
        if index<0:
            index = self.n + index 
        return self.insert(index,value)
        
    def __delitem__(self,pos):
        if self.n == 0:
            return 'Empty List'
        if 0<= pos < self.n:
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]
            self.n -= 1 
            
    
    def index(self,value):
        for i in range(self.n):
            if self.A[i]==value:
                return i 
        return 'Value not found'
    
    def insert(self,pos,item):
        if self.size == self.n:
            self.__resize_array(self.size*2)
            
        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]
        
        self.A[pos] = item 
        self.n += 1 
        
    
    def remove(self,value):
        pos = self.index(value)
        if type(pos) == int:
            self.__delitem__(pos) 
        return pos 
    
    def sort(self):
        for i in range(self.n):
            for j in range(self.n-i-1):
                if self.A[j]>self.A[j+1]:
                    self.A[j],self.A[j+1]=self.A[j+1],self.A[j]
        return 
    
    def min(self):
        min_val = self.A[0]
        for i in range(self.n):
            if self.A[i]<min_val:
                min_val = self.A[i]
        return min_val 
        
    def max(self):
        max_val = self.A[0]
        for i in range(self.n):
            if self.A[i]>max_val:
                max_val = self.A[i]
        return max_val 
    
    def sum(self):
        sum = 0
        for i in range(self.n):
            sum += self.A[i]
        return sum 
        
  
    def extend(self, other):
        if isinstance(other, List):
            # Agar dusra bhi List class ka hai
            for i in range(other.n):
                self.append(other[i])
        elif hasattr(other, '__iter__') and not isinstance(other, (str, bytes)):
            # Agar Python list, tuple, set, etc. hai
            for item in other:
                self.append(item)
        else:
            # Agar single value hai
            self.append(other)
        return self.A

    def merge(self, other):
        new_list = List()
        # pehle apne elements add karo
        for i in range(self.n):
            new_list.append(self[i])
    
         # ab doosre ke elements add karo
        if isinstance(other, List):
            for i in range(other.n):
                new_list.append(other[i])
        elif hasattr(other, '__iter__') and not isinstance(other, (str, bytes)):
            for item in other:
                new_list.append(item)
        else:
            new_list.append(other)
    
        return new_list
        
    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()
    
    def __resize_array(self,new_capacity):
        # create new array with new capacity
        B = self.__make_array(new_capacity)
        # update size 
        self.size = new_capacity
        # copies elements from A
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A 
        self.A = B 
        

L = List()
L.append(1)   
L.append(2)
L.append(3)
print(L)
print('Length: ',len(L))
print('pop last element')
L.pop()
print('-------------')
print(L)
L.append(4)
L.append(5)
print(L[0])
print(L[-1])
print(L[::-1])
print('Find Position Via Value')
print(L.index(5))
print(L.index(1))
L.insert(2,'hello')
L.insert(3,'python')
L[6] = 'django'
print(L)
del L[1]
print(L)
L.remove('django')
L.remove('hello')
L.remove('python')
print(L)
print(L.min())
print(L.max())
print(L.sum())
L.append(2)
L.append(0)
print(L)
L.sort()
print(L) 
print('------ Extend -----')
L.extend([15,16,17])
print(L)
print('------ merge ------')
print(L.merge([21,22,23]))
print(L)

