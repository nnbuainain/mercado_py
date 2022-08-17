class Cart():

    def __init__(self, cart_products):
        self.__cart_products = cart_products
        #self.__total = get_total()
    @property
    def cart_products(self):
        return self.__cart_products

        
def get_total(self):
    total = 0
    for product in self.__cart_products:
        total += product.price
    return total