class Student:
    def _init_(self, id, name) -> None:
        self.Id = id
        self.Name = name


class StudentQueue:
    def __init__(self):
        self.size = 5
        self.queue = []

    def IsEmpty(self):
        size = len(self.queue)
        if size == 0:
            return True
        return False

    def Dequeue(self):
        if self.IsEmpty():
            print("The queue is empty!!")
            return None
        return self.queue.pop(0)

    def Enqueue(self, data):
        if len(self.queue) >= self.size:
            print(f" queue is full!! Size {self.size}!!")
        else:
            self.queue.append(data)

    def display_all(self):
        if self.IsEmpty():
            print("The queue is empty!!")
        else:
            print("Queue Contents:")
            for student in self.queue:
                print(f"ID: {student.Id}, Name: {student.Name}")

    def free_queue(self):
        self.queue = []
        print("Queue is freed successfully!")




if __name__ == "__main__":
    student_queue = StudentQueue()

    student_queue.Enqueue((1, "heba"))
    student_queue.Enqueue(2, "maria")
    student_queue.Enqueue(3, "nour")

    student_queue.display_all()

    student_queue.Dequeue()
    student_queue.display_all()

    student_queue.free_queue()
    student_queue.display_all()


