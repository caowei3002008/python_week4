class animal(object):
    def __init__(self, name, health):
        self.name = name;
        self.health = health;
    def walk(self):
        self.health -=1
        return self
    def run(self):
        self.health -=5
        return self
    def display_health(self):
        print "The health for the animal of", self.name,"is",self.health
        return self
animal1 = animal('fish',100)
animal1.walk().walk().walk().run().run().display_health()

class dog(animal):
    def __init__(self, name, health = 150):
        super(dog,self).__init__(name, health)
    def pet(self):
        self.health +=5
        return self
dog1 = dog('dogdog')
dog1.walk().walk().walk().run().run().display_health()
class dragon(animal):
    def __init__(self,name, health = 170):
        super(dragon,self).__init__(name, health)
    def fly(self):
        self.health -10
        return self
    def display_health(self):
        super(dragon,self).display_health()
        print "I am a Dragon"
        return self
dragon1 = dragon('dragon123')
dragon1.fly().display_health()
# animal2 = animal('fish1',1000)
# animal2.fly().pet() 



