class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
  
class LinkedList:   
    def __init__(self): 
        self.head = None
        
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    def append(self,val):
        temp=Node(val)
        p=list.head
        while(p.next):
            p=p.next
        p.next=temp
        temp.prev=p
        
      
        
        
    def insert(self,val,pos):
        if(list.head.next==None):
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
        if(pos==0 or list.head.next==None):
            print("can't delete head node")
        else:
            p=list.head
            q=list.head.next
            npos=0
            while(npos!=pos-1):
                p=p.next
                if(q.next==None):
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

list.append(40)
list.printlist()
print("---------")


list.insert(30,2)
list.printlist()
print("---------")

list.delete(2)
list.printlist()
print("---------")

list.delete(4)
list.printlist()
print("---------")

list.insert(60,1)
list.printlist()
print("---------")