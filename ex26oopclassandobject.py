class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
     
    def greet(self):
        print(f"hello,my name is {self.name} and i am {self.age} years old.")
        
person=Person("Alice",21)
person.greet()
 


