class Student:
    def __init__(self, name, age, grade, email):
        self.name = name
        self.age  = age
        self.grade = grade
        self.email = email

    def display(self):
        print(f'Name:{self.name}, Age:{self.age}, Grade:{self.grade}, Email:{self.email}')

class Catalog:
    def __init__(self):
     self.students = []

    def add_student(self,student):

             self.students.append(student)


    def display_all(self):
        for student in self.students:
            student.display()

catalog = Catalog()
catalog.add_student(Student('Alex', '20', 10,  'alex43@gmail.com'))
catalog.add_student(Student('Maria','20', 9, 'maria33@gmail.com'))
catalog.display_all()
