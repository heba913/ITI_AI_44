class node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class singlylist:
    def __init__(self) -> None:
        self.head=None
    
    def append(self , data):
        nd=node(data)
        if self.head==None:#appending at an empty list
            self.head=nd
        else:
            counter=self.head
            while counter.next:#appending at the end of a non-empty list
                counter = counter.next
            counter.next=nd

    
    def insert(self , data , loc):#inserts after the loc
        nd = node(data)
        if self.head==None:#inserting at an empty linked list
            self.head=nd
        else:
            if loc == 0 :#inserting at the frist place
                nd.next=self.head
                self.head=nd
            else:
                current=self.head
                count=0
                while count < loc-1 and current is not None:#loop untill the end of the list
                    current=current.next
                    count +=1
                nd.next=current.next
                current.next=nd
    
    def delete(self , data):
        if self.head== None:
            print("list is empty ")
        else:
            current=self.head
            if current.data == data:#data found in frist position 
                self.head=self.head.next
            else:
                while current.next:
                    if current.next.data==data:
                        current.next=current.next.next
                    current=current.next
    
    def search(self,data):
        if self.head== None:
            print("list is empty ")
        else:
            current=self.head
            while current :
                if current.data == data:
                    print(f"{data} found successfully")
                
                current=current.next



    

    def traverse(self):
        current = self.head
        print("****list items****")
        while current:
            print(current.data,"\n ")
            current = current.next
        
        






sll = singlylist()
sll.append(1)
sll.append(2)
sll.append(3)
sll.insert(4,2)
sll.delete(4)
sll.traverse()
sll.search(1)