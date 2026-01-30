class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age  = age
        self.grade = grade

    def display(self):
        print(f'Name:{self.name}, Age:{self.age}, Grade:{self.grade}')

class Catalog:
    def __init__(self):
     self.students = []

    def add_student(self,student):
        if student.name[0].lower() not in 'aeiou':
             self.students.append(student)
        else:
             print('Error')


    def display_all(self):
        for student in self.students:
            student.display()

catalog = Catalog()
catalog.add_student(Student('Alex', '20', 10))
catalog.add_student(Student('Maria','20', 9))
catalog.display_all()

