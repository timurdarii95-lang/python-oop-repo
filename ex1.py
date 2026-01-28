class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color


car1 = Car(brand='Toyota', color='red')
car2 = Car(brand='Honda', color='blue')


print(car1.brand)
print(car2.color)