# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# YOUR NAME

class LinkedList:

    def __init__(self, value = None):
        self.value = value
        self.next = self
        self.prev = self
        self.size = 0

    def is_sentinel(self):
        if self.value == None:
            return True
        else:
            return False
        
    def is_empty(self):
        return self.next is self and self.prev is self
       
    def is_last(self):
        return self.next.is_sentinel()

    def last(self):
        if self.is_last():
            return self
        return self.next.last()
            

    def append(self, appendee):
        if self.is_empty() == True:
            self.prev = appendee
            self.next = appendee
            appendee.prev = self
            appendee.next = self
            self.size += 1
        elif self.is_sentinel():
            self.size += 1
            self.prev = appendee
            appendee.next = self
            self = self.last()
            self.next = appendee
            appendee.prev = self
            return self.next.append(appendee)

   
    def delete(self):
        self.next.prev = self.prev
        self.prev.next = self.next
        

    def insert(self, ins):
        ins.prev = self
        ins.next = self.next
        self.next.prev = ins
        self.next = ins


    def at(self, N):
        x = 0
        while x < N:
            self = self.next
            x += 1
        return self
        
    def search(self, value):
        if self.value == value:
            return self
        elif self.next.value is None: 
            return None
        return self.next.search(value)
            

    def insert_in_order(self, ins):
        if self.next is self:
            self.append(ins)
        elif ins.value >= self.next.value and self.next is not self:
            self = self.next
            self.insert_in_order(ins)
        elif ins.value <= self.next.value:
            self.insert(ins)
         
        
        
        
         



        
        



    

    
    

    


    


    

    

    
