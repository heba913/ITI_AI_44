class node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        self.prev=None
    

class doublylist:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    
    def append(self , data):#adding item at the end of the list
        nd=node(data)
        if self.head==None:
            self.head=nd
            self.tail=nd
        else:
            self.tail.next=nd
            nd.prev=self.tail
            self.tail=nd
    
    def insert(self,data,loc):
        nd=node(data)
        if self.head==None:
            self.head=nd
            self.tail=nd
        else:
            if loc == 0 :
                nd.next=self.head
                self.head.prev=nd
                self.head=nd
            else:
                current=self.head
                counter=0
                while counter < loc-1 and current.next is not None:
                    current=current.next
                    counter+=1
                    if current==self.tail:
                        self.tail.next=nd
                        nd.prev= self.tail
                        current.next=nd
                    else:
                        

                        nd.next = current.next
                        current.next.prev = nd
                        nd.prev = current
                        current.next = nd
    
    def delete(self,data):
        if self.head == None:
            print("list is empty")
        else:
            current=self.head
            if current.data == data:
                if current.next == None:
                    self.head=None
                    self.tail=None
                else:
                    self.head=current.next
                    current.prev=None
            while current:
                if current.data == data:
                    if current==self.tail:
                        self.tail=current.prev
                        self.tail.next=None
                    else:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                current=current.next
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next

                






    def traverse(self):
        current=self.head
        print("*****list elements*****")
        while current:
            
            print(current.data,"\n")
            current=current.next



fruits=doublylist()
fruits.append('banana')
fruits.append('apple')
fruits.insert('watermelon',2)
fruits.delete('banana')
fruits.traverse()