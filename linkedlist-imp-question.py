# LinkedIn 

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None 
        
class LinkedList:
    def __init__(self):
        self.head=None 
        self.n=0
        
    def insert(self,value):
        new_node = Node(value)
        
        if self.head==None:
            self.head = new_node
            return 
            
        
        curr = self.head 
        
        while curr.next!=None:
            curr=curr.next 
        curr.next = new_node
        self.n+=1
    
    def view(self):
        res=''
        curr=self.head
        while curr!=None:
            res = res + str(curr.data) + '->'
            curr=curr.next
            
        return res[:-2] 
    
   
    def create_cycle(self,pos):
        
        curr = self.head 
        cycle_node=None
        index=0
        
        if pos==-1:
            return 
        
        while curr:
            
            if index==pos:
                cycle_node = curr
                
            if curr.next is None:
                break 
            
            curr=curr.next 
            index+=1 
            
        curr.next = cycle_node 
            
    def detect_cycle(self):
        slow=self.head
        fast=self.head
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            
            if slow==fast:
                return True
                
        return False 
    
    def remove_cycle(self):
        slow=self.head 
        fast=self.head 
        
        # detect cycle 
        while fast and fast.next:
            slow=slow.next
            fast = fast.next.next 
            
            if slow==fast:
                break 
        else:
            return # no cycle 
        
        # step-2 move one pointer to head 
        slow = self.head 
        while slow!=fast:
            slow=slow.next 
            fast=fast.next 
            
        # step-3 find last node of cycle 
        while fast.next!=slow:
            fast=fast.next 
        
        fast.next=None
        
    
    def reverse(self):
        # store prev value
        prev=None
        # curr
        curr=self.head
        
        # loop
        while curr:
            # store next node
            next_node = curr.next
            # st0ore prev value in curr.next 
            curr.next = prev
            # prev = 
            prev = curr 
            curr = next_node
            
        self.head = prev 
        
    
    def merge(self,left,right):
        # create dummy 
        dummy = Node(0)
        tail = dummy 
        while left and right:
            if left.data < right.data:
                tail.next = left
                left = left.next 
            else:
                tail.next = right 
                right = right.next 
                
            tail = tail.next
        
        # for remaining elements
        tail.next = left if left else right 
        return dummy.next 
        
    
    def get_middle(self,head):
        if not head or not head.next:
            return head 
        
        slow=head 
        fast = head.next 
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        return slow 
    
    def merge_sort(self,head):
        # 0 (empty) and 1(only 1 value) in node is already sorted 
        if not head or not head.next:
            return head 
        
        #1 split list into two halves 
        mid = self.get_middle(head)
        right_head = mid.next 
        mid.next = None # break list into two parts 
        
        #2. Recursively sort each half 
        left_sorted = self.merge_sort(head)
        right_sorted = self.merge_sort(right_head)
        
        #3. merge the two halves
        return self.merge(left_sorted,right_sorted)
        
    def sort(self):
        self.head = self.merge_sort(self.head)
        
    def sort_easy(self):
        arr=[]
        curr=self.head
        while curr:
            arr.append(curr.data)
            curr=curr.next 
        
        # sort array 
        arr.sort()
        
        curr = self.head 
        i=0 
        while curr:
            curr.data = arr[i]
            i+=1 
            curr=curr.next 
            
        
        
        
        
l1 = LinkedList()
l1.insert(1)
l1.insert(2)
print(l1.view())
l1.insert(3)
l1.insert(4)
print(l1.view())

l1.create_cycle(2)

print(l1.detect_cycle()) # True

l1.remove_cycle()

print(l1.detect_cycle()) # False 

l1.reverse()


print(l1.view())

l2 = LinkedList()
l2.insert(19)
l2.insert(11)
l2.insert(21)
l2.insert(5)

print('Before Sort: ',l2.view())

# l2.sort_easy()

l2.sort()

print('After Sort: ',l2.view())


    
        