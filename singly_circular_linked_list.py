class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = self  
  
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
        temp=Node(val)
        p=list.head
        while(p.next!=list.head):
            p=p.next
        p.next=temp
        temp.next=list.head
        
        
    def removeNthFromEnd(self, n):
        temp=list.head
        if(temp.next==list.head):
            print("only head exist")
        else:
            p=q=list.head
            pos=1
            while(q.next!=list.head):
                q=q.next
                pos=pos+1
            #print(pos)
            tobedelete=pos-n
            list.delete(tobedelete)
            
    
    def delete(self,pos):
        if(pos==0 or list.head.next==list.head):
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
            p.next=q.next
            q=q.next
        
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

list.append(60)
list.printlist()
print("---------")

list.delete(3)
list.printlist()
print("---------")

list.removeNthFromEnd(4)
list.printlist()
print("---------")
