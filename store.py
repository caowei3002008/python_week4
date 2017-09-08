class store(object):
    def __init__(self, products, location, owner,shopping_list = []):
        self.products = products
        self.location = location
        self.owner = owner
        self.shopping_list = shopping_list
    def add_product(self,product_name):
        if product_name in self.products:
            self.shopping_list.append(product_name)
        for product_name in self.shopping_list:
            print product_name
        return self
    def remove_product(self,product_name):
        if product_name in self.shopping_list:
            self.shopping_last.remove(product_name)
        for product_name in self.shopping_list:
            print product_name

        return self
    def inventory_display(self):
        for item in self.products:
            print item
        return self
    def store_info(self):
        print 'Store Location: ', self.location, " , Owner's name:", self.owner
        return self

store1 = store(['a','b','c','d','e','f','g','h','i','j','k'],'Burbank','Trump')
# store1.store_info().inventory_display()
# store1.add_product('a').add_product('b')