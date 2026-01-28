class Animal:
    def __init__(self, species):
        self.species = species

    def sound(self):
        print('Animaliul produce un sunet')

class Dog (Animal):
    def sound(self):
        print('Ham-ham!')

dog = Dog('DALMATIAN')
dog.sound()

