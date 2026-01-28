class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engin(self):
            print(f'THE {self.color}{self.brand} is starting!')

car1 = Car('Toyota',  'red')
car2 = Car('Honda',  'blue')
car3 = Car('Ford', 'green')

parking_lot =[car1, car2, car3]

for car in parking_lot:
    car.start_engin()

