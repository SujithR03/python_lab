class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
class student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name,age)
        self.student_id=student_id
        
    def display_id(self):
        print(f"my student id is {self.student_id}.")
        
student1=student("bob",20,"s12345")
student1.display_id()
