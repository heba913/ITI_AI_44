import time
class node:
    def __init__(self , data):
        self.data=data
        self.prev=None


class stack:
    def __init__(self):
        self.tail=None

    def push(self,id,name):
        nd=node((id,name))
        if self.tail==None:
            self.tail=nd
        else:
            nd.prev=self.tail
            self.tail=nd

    def pop(self):
        nd=self.tail
        if(self.tail != None):
            self.tail=self.tail.prev

        return nd

    def display(self):
        current = self.tail
        while current:
            print(f"ID: {current.data[0]}, Name: {current.data[1]}")
            time.sleep(2)
            current = current.prev


    def free(self):
        current=self.tail
        while current:
            self.pop()
            current=current.prev
        print('stack is now free')






# stack=stack()
# stack.push(1,'ali')
# stack.push(2,'manar')
# stack.push(3,'maria')
# stack.free()
# stack.display()




if __name__ == "__main__":
    my_stack = stack()

    while True:
        print("\nMy linked list :")
        print("1. Add ")
        print("2. display ")
        print("3. Delete ")
        print("4. free")
        print("4. exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            id = int(input("Enter  ID : "))
            name = input("Enter  name : ")
            my_stack.push(id,name)
        elif choice == "2":
            print("\nAll nodes:")
            my_stack.display()

        elif choice == "3":
           my_stack.pop()
           print("node poped ")

        elif choice == "4":
            stack.free()
            print("stack is freed ")

        elif choice == "5":
            print("Good bye")
            break
        else:
            print("Invalid choice! Please enter a valid option.")


