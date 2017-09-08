class car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.display_all()

    def display_all(self):
        print 'Price:',self.price
        print 'Speed:',self.speed
        print 'Fuel:',self.fuel
        print 'Mileage:',self.mileage
        if self.price > 10000:
            tax = 0.15
        elif self.price <10000 or self.price > 0:
            tax = 0.12
        print 'Tax:', tax

car1 = car(2000,'35mph','Full','15mpg')
# car1.display_all()
car2 = car(2000,'5mph','Not Full','105mpg')
# car2.display_all()
car3 = car(2000,'15mph','Kind of Full','95mpg')
# car3.display_all()
car4 = car(2000,'25mph','Full','25mpg')
# car4.display_all()
car5 = car(2000,'45mph','Empty','25mpg')
# car5.display_all()
car6 = car(20000000,'35mph','Empty','15mpg')
# car6.display_all()
