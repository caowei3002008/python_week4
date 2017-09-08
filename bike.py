class bike(object):
    def __init__(self,price,max_speed,miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print "The bike's price is",self.price,", the maximum speed is",self.max_speed,", and the total miles is",self.miles
        return self
    def ride(self):
        self.miles +=10
        return self
    def reverse(self):
        self.miles -=5
        return self
bike1 = bike(1000,50)
bike2 = bike(1200,60)
bike3 = bike(1300,70)
bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
