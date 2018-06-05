#implement cyclic right shift for singly linked lists

class node():
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
	    current = self.head
	    count = 0
	    while current:
	        count += 1
	        current = current.get_next()
	    return count
	
    def display(self):
        curr=self.head
        while curr!=None:
            print curr.get_data(),
            curr=curr.get_next()

    def rotate(self,x):
        curr=self.head
        prev=curr
        for i in range(self.size()-x):
            prev=curr
            curr=curr.get_next()
        t2=curr
        prev.set_next(None)
        if t2:
            while t2.get_next() is not None:
                t2=t2.get_next()
            t2.set_next(self.head)
            self.head=curr
            
a=list(map(int,raw_input().split()))
l=LinkedList()

for i in a:
    l.insert(i)
l.display()
print

x=input()
if l:
    x=x%(l.size())
    print x
    l.rotate(x)
    l.display()
else:
    print [] 


    
    
