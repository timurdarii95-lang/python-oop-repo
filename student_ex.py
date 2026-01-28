class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello , my name is {self.name} and I am {self.age} years old.')



student1 = Student('Alex', 20)
student1.greet()