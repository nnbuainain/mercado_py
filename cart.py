class Cart():
    
    def __init__(self, cart_products):
        self.__cart_products = cart_products
        self.__total = 0
    
    @property
    def cart_products(self):
        return self.__cart_products    

    @property
    def total(self):
        #self.__total = 0
        for product in self.__cart_products:
            self.__total += product['total_price']
        return self.__total

    def show_cart(self):
        if len(self.__cart_products) != 0:

            for product in self.__cart_products:
                print(f"Code: {product['code']} \t Name: {product['name']}\
                    \t Quantity: {product['quantity']} \t Unit Price: {product['unit_price']}\
                    \t Total Price: {product['total_price']}")
            
            print(f"\n Total in your cart: {self.total}")
            
        else:
            print('\n ########## There is no product in the cart yet ##########')