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
        

def reverse_string(text):
    s = Stack()
    
    for i in text:
        s.push(i)
    
    res = ''
    while (not s.is_empty()):
        res = res + s.pop()
    return res

def text_editor(text,pattern):
    u = Stack()
    r = Stack()
    
    for i in text:
        u.push(i)
    
    for i in pattern:
        if i == 'u':
            data = u.pop()
            r.push(data)
        elif i=='r':
            data = r.pop()
            u.push(data)
    
    res = ''
    while (not u.is_empty()):
        res = u.pop() + res
    return res
    

def find_celeb(L):
    s= Stack()
    
    for i in range(len(L)):
        s.push(i)
    
    while s.size()>=2:
        i = s.pop()
        j = s.pop()
        
        if L[i][j]==0:
            # means i not knows j - j not celebrity
            s.push(i)
        else:
            # neans j not knows i - i is not celibrity 
            s.push(j)
    
    celeb = s.pop()
    for i in range(len(L)):
        if i!=celeb:
            if L[i][celeb]==0 or L[celeb][i]==1:
                print('No one is celibrity')
                
    print('the celebrity is ',celeb)
  

def valid_parenthesis(text):
    s = Stack()
    mappings = {
        ']':'[',
        '}':'{',
        ')':'('
    }
    
    for i in text:
        if i in mappings:
            if not s or s.pop()!=mappings[i]:
                return False
        else:
            s.push(i)
            
    return s.size()==0
        
        
  
print(reverse_string('python'))
print(text_editor('hello','uur'))

## celibrity matrix 
L = [
    [0,0,1,0],
    [0,1,1,0],
    [0,0,0,0],
    [0,1,1,0]
    ]
    
find_celeb(L)
    
print(valid_parenthesis('({})'))
print(valid_parenthesis('({})('))       
