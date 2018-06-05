#Test for overlapping lists - lists are cycle-free

class Node():
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
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def display(self):
        curr=self.head
        while curr!=None:
            print curr.data
            curr=curr.next_node  

    def size(self):
	    current = self.head
	    count = 0
	    while current:
	        count += 1
	        current = current.get_next()
	    return count

def findoverlap(biglist,bign,smallist,smallen):
    curr1=biglist.head
    while bign-smallen>0:
        curr1=curr1.get_next()
        bign-=1
    curr2=smallist.head
    flag=0
    for i in range(bign):
        if curr1==curr2:
            flag=1
            break
        curr1=curr1.get_next()
        curr2=curr2.get_next()
    if flag:
        return curr1
    else:
        return None
    

a=map(int,raw_input().split())
alist=LinkedList()
for x in a:
    alist.insert(x)
b=map(int,raw_input().split())
blist=LinkedList()
for x in b:
    blist.insert(x)
    
if not alist or not blist:
    print "No overlap"

else:
    alen=alist.size()
    blen=blist.size()
    if alen>=blen:
        ans=findoverlap(alist,alen,blist,blen)
    else:
        ans=findoverlap(blist,blen,alist,alen)

    if ans is None:
        print "No overlap"
    else:
        print ans.get_data()


