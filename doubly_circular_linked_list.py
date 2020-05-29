class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = self
        self.prev = self
  
class LinkedList:   
    def __init__(self): 
        self.head = None
    
    def printlist(self):
        temp=list.head
        while(temp.next!=list.head):
            print(temp.data)
            temp=temp.next
        print(temp.data)
        
    def append(self,val):
        print("in append")
        temp=Node(val)
        p=list.head
        while(p.next!=list.head):
            p=p.next
        p.next=temp
        temp.prev=p
        temp.next=list.head
        list.head.prev=temp
        
        
    def insert(self,val,pos):
        if(list.head.next==list.head):
            list.append(val)
        else:
            temp=Node(val)
            npos=0
            p=list.head
            q=list.head.next
            while(npos!=pos-1):
                p=p.next
                q=q.next
                npos=npos+1
            p.next.prev=temp
            temp.next=q
            p.next=temp
            temp.prev=p

            
    
    def delete(self,pos):
        if(pos==0 or list.head.next==list.head):
            print("can't delete head node")
        else:
            p=list.head
            q=list.head.next
            npos=0
            while(npos!=pos-1):
                p=p.next
                if(q.next==list.head):
                    print("exceeded noeds")
                    return
                q=q.next
                npos=npos+1
            q.next.prev=q.prev
            p.next=q.next

    
    
list=LinkedList()
list.head=Node(10)
list.printlist()
print("---------")

list.append(20)
list.printlist()
print("---------")

list.append(30)
list.printlist()
print("---------")

list.append(40)
list.printlist()
print("---------")

list.append(50)
list.printlist()
print("---------")

list.insert(22,2)
list.printlist()
print("---------")

list.delete(5)
list.printlist()
print("---------")
