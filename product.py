class product(object):
    def __init__(self,price, item_name, weight, brand, cost = 0, status = "for sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
    def sell(self):
        self.status = 'sold'
        return self
    def addTax(self,tax):
        self.cost = (1+tax)*self.price
        return self
    def product_return(self,reason):
        if reason in ['defective', 'd']:
            self.price = 0
            self.status = 'for defective'
        elif reason in ['box']:
            self.status = 'for sale'
        elif reason in ['opened']:
            self.status = 'used'
            self.price = 0.8 * self.price
        return self
    def display_info(self):
        print 'Price:', self.price
        print 'Item Name:', self.item_name
        print 'Weight:', self.weight
        print 'Brand:', self.brand
        print 'Cost:', self.cost
        print 'Status:', self.status
product1 = product(1000,'game','5oz','game stop')
product1.addTax(.0775).display_info()
product2 = product(100,'book','10oz','game stop')
product2.product_return('opened').addTax(.0775).display_info()

