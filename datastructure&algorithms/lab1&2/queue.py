import time
class node:
    def __init__(self , data):
        self.data=data
        self.next=None


class queue :
    def __init__(self):
        self.head=None
        self.tail=None

    def enqueue(self,id,name):
        nd=node((id,name))
        if self.head == None:
            self.head=nd
            self.tail=nd
        else:
            self.tail.next=nd
            self.tail=nd

    def dequeue(self):
        nd = self.head
        if self.head !=  None:
            self.head=self.head.next
            if self.head == None:
                self.tail=None

        return nd

        