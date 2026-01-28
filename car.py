class Car:

    # nume_masina     = 'Mercedes'
    # tip_combustibil = 'benzina'
    # an_fabricatie   = 2017

    # init sau constructor
    def __init__(self, nume_masina, tip_combustibil, an_fabricatie):
        self.nume_masina     = nume_masina
        self.tip_combustibil = tip_combustibil
        self.an_fabricatie   = an_fabricatie


    def porneste_motorul(self, tip_combustibil):
        print(self.nume_masina,
              self.tip_combustibil,
              self.an_fabricatie,
              "Motor pornit.", tip_combustibil)

    def opreste_motorul(self):
        print("Motor oprit.")



car_1 = Car('Audi','diesel',2025)
car_1.porneste_motorul('clasic')

car_2 = Car('Tesla','eco', 2024)
car_2.porneste_motorul('electric')